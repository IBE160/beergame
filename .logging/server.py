#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Simple HTTP server for API Request Viewer

Serves the .logging directory with CORS headers enabled and automatically
opens the viewer in your default browser.

Usage:
    uv run .logging/server.py [port]
    python .logging/server.py [port]

Default port: 8000
"""

import sys
import json
import re
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import unquote, quote


def sanitize_title(title):
    if not title or not title.strip():
        return None
    title = title.strip()
    if len(title) > 100:
        title = title[:100]
    safe_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
    result = ""
    for char in title:
        if char in safe_chars:
            result += char
        elif char == " ":
            result += "-"
        else:
            result += "_"
    result = re.sub(r"[-_]+", "-", result)
    result = result.strip("-_")
    return result if result else None


def parse_session_filename(filename):
    name = filename.replace(".json", "")
    if "--" in name:
        base_part, title_part = name.split("--", 1)
        title = title_part.replace("-", " ")
    else:
        base_part = name
        title = None
    match = re.match(r"(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})-(.+)$", base_part)
    if match:
        timestamp_str, session_id = match.groups()
        return {"timestamp": timestamp_str, "session_id": session_id, "title": title}
    return None


def build_session_filename(timestamp, session_id, title=None):
    base = f"{timestamp}-{session_id}"
    if title:
        sanitized = sanitize_title(title)
        if sanitized:
            return f"{base}--{sanitized}.json"
    return f"{base}.json"


class CORSRequestHandler(SimpleHTTPRequestHandler):
    """HTTP request handler with CORS headers enabled."""

    def end_headers(self):
        """Add CORS headers to all responses."""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, PUT, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_GET(self):
        """Handle GET requests, including API endpoints."""
        # API endpoint to list JSON files
        if self.path == '/api/files':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Get all JSON files from requests/ folder
            requests_dir = Path('requests')
            if requests_dir.exists():
                files = []
                for json_file in sorted(requests_dir.glob('*.json'), reverse=True):
                    stat = json_file.stat()

                    # Parse filename to extract session info
                    parsed = parse_session_filename(json_file.name)
                    if parsed:
                        timestamp_str = parsed['timestamp']
                        year, month, day = timestamp_str.split('_')[0].split('-')
                        time_part = timestamp_str.split('_')[1]
                        hour, minute, second = time_part.split('-')
                        timestamp = f"{year}-{month}-{day}T{hour}:{minute}:{second}"

                        files.append({
                            'filename': json_file.name,
                            'timestamp': timestamp,
                            'sessionId': parsed['session_id'],
                            'title': parsed['title'],
                            'size': stat.st_size
                        })
                    else:
                        # Fallback for old format
                        match = re.match(r'(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2})-(.+)\.json', json_file.name)
                        if match:
                            year, month, day, hour, minute, second, session_id = match.groups()
                            timestamp = f"{year}-{month}-{day}T{hour}:{minute}:{second}"
                            files.append({
                                'filename': json_file.name,
                                'timestamp': timestamp,
                                'sessionId': session_id,
                                'title': None,
                                'size': stat.st_size
                            })

                self.wfile.write(json.dumps(files).encode())
            else:
                self.wfile.write(b'[]')
            return

        # Default file serving
        super().do_GET()

    def do_PUT(self):
        """Handle PUT requests for API endpoints."""
        # API endpoint to rename session file
        if self.path == '/api/sessions/rename':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data.decode('utf-8'))
                current_filename = data.get('currentFilename')
                new_title = data.get('newTitle')

                if not current_filename:
                    self.send_error(400, 'Missing currentFilename')
                    return

                if not new_title or not new_title.strip():
                    self.send_error(400, 'Missing or empty newTitle')
                    return

                # Parse current filename
                parsed = parse_session_filename(current_filename)
                if not parsed:
                    self.send_error(400, 'Invalid filename format')
                    return

                # Build new filename
                new_filename = build_session_filename(
                    parsed['timestamp'],
                    parsed['session_id'],
                    new_title
                )

                # Rename the file
                requests_dir = Path('requests')
                old_path = requests_dir / current_filename
                new_path = requests_dir / new_filename

                if not old_path.exists():
                    self.send_error(404, 'File not found')
                    return

                if new_path.exists() and new_path != old_path:
                    self.send_error(409, 'File with that name already exists')
                    return

                old_path.rename(new_path)

                # Return success with new filename
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {
                    'success': True,
                    'newFilename': new_filename,
                    'title': new_title
                }
                self.wfile.write(json.dumps(response).encode())

            except json.JSONDecodeError:
                self.send_error(400, 'Invalid JSON')
            except Exception as e:
                self.send_error(500, str(e))
            return

        # Unknown endpoint
        self.send_error(404, 'Not found')


    def do_OPTIONS(self):
        """Handle OPTIONS requests for CORS preflight."""
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        """Customize log messages to be more concise."""
        if args[1] == '200':
            # Only log non-200 responses to reduce noise
            return
        super().log_message(format, *args)


def main():
    # Fix encoding for Windows console
    import io
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

    # Parse port from command line args
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number: {sys.argv[1]}")
            print("Usage: python server.py [port]")
            sys.exit(1)

    # Change to .logging directory
    script_dir = Path(__file__).parent
    import os
    os.chdir(script_dir)

    # Create server
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, CORSRequestHandler)

    # Print startup message
    url = f'http://localhost:{port}/api-viewer.html'
    print('='*60)
    print('🚀 API Request Viewer Server')
    print('='*60)
    print(f'Server running at: http://localhost:{port}')
    print(f'Viewer URL: {url}')
    print('\nPress Ctrl+C to stop the server')
    print('='*60)

    # Open browser
    print('\n📱 Opening browser...')
    webbrowser.open(url)

    # Run server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n\n👋 Shutting down server...')
        httpd.shutdown()
        print('✅ Server stopped')


if __name__ == '__main__':
    main()
