# Gemini CLI Telemetry Processing Scripts

This directory contains scripts for processing and analyzing Gemini CLI telemetry logs.

## Scripts

### `process-api-requests.py`

Extracts API request, response, and error events from the telemetry log file and outputs them as structured JSON grouped by `prompt_id`.

**Features:**
- ✅ File locking to prevent concurrent access
- ✅ Groups request/response/error events by `prompt_id`
- ✅ Outputs timestamped JSON files
- ✅ Progress feedback during processing
- ✅ Automatic log file clearing after successful processing
- ✅ Handles incomplete JSON gracefully

### `watcher.py`

Real-time watcher that monitors telemetry logs and organizes them into session folders. See script header for details.

## File Structure

The logging directory is organized as follows:

```
.logging/
├── process-api-requests.py  # Main processing script
├── watcher.py               # Real-time telemetry watcher
├── server.py                # HTTP server for viewer
├── api-viewer.html          # Interactive web viewer
├── requests/                # Generated API request files
│   └── api-requests-*.json  # Individual request/response logs
├── log.jsonl                # Raw telemetry log file
└── README.md                # This file
```

## Quick Start

### Running with `uv` (Recommended)

No setup required! Just run:

```bash
uv run .logging/process-api-requests.py
```

The `uv` tool automatically handles dependencies defined in the script header. Output files are saved to `.logging/requests/` and can be viewed via the API Request Viewer.

### Options

```bash
# Don't clear the log file after processing
uv run .logging/process-api-requests.py --no-clear

# Specify custom output directory
uv run .logging/process-api-requests.py --output-dir ./my-output

# Enable verbose debug output
uv run .logging/process-api-requests.py --verbose

# Keep JSON strings raw (don't parse into objects)
uv run .logging/process-api-requests.py --raw

# Combine options
uv run .logging/process-api-requests.py --no-clear --verbose --output-dir ./output

# Show help
uv run .logging/process-api-requests.py --help
```

## Setting Up for Debugging in VSCode

### 1. Create a Virtual Environment (Optional)

If you want to debug in VSCode with breakpoints:

```bash
# Create virtual environment
python -m venv .logging/.venv

# Activate it (Windows Git Bash)
source .logging/.venv/Scripts/activate

# Or on Linux/Mac
source .logging/.venv/bin/activate

# Install dependencies
pip install -r .logging/requirements.txt
```

### 2. Configure VSCode Debugger

A debug configuration has been added to `.vscode/launch.json`. To use it:

1. Open the script in VSCode: `.logging/process-api-requests.py`
2. Set breakpoints by clicking in the gutter
3. Press `F5` or go to **Run > Start Debugging**
4. Select **"Python: Process API Requests"** from the dropdown

### 3. Debug Configuration Options

The debug config includes several launch configurations:

- **Process API Requests (Default)**: Normal run with log clearing
- **Process API Requests (No Clear)**: Run without clearing the log
- **Process API Requests (Verbose)**: Run with verbose debug output

## JSON Parsing Feature

By default, the script **automatically parses JSON strings** embedded in telemetry fields into proper JSON objects. This makes the output much more readable and easier to work with.

### What Gets Parsed

The following fields are automatically parsed from strings to objects:
- `request_text` - The API request payload
- `response_text` - The API response data
- `function_args` - Tool function arguments

### Example

**Without parsing (--raw flag):**
```json
{
  "request_text": "[{\"role\":\"user\",\"parts\":[{\"text\":\"Hello\"}]}]"
}
```

**With parsing (default):**
```json
{
  "request_text": [
    {
      "role": "user",
      "parts": [
        {"text": "Hello"}
      ]
    }
  ]
}
```

### Disabling Parsing

If you need the original string format (for compatibility or debugging), use the `--raw` flag:
```bash
uv run .logging/process-api-requests.py --raw
```

## Output Format

The script generates files in `.logging/requests/` named `api-requests-YYYY-MM-DD_HH-mm-ss.json` with this structure:

```json
[
  {
    "prompt_id": "abc123",
    "request": {
      "model": "gemini-2.0-flash-exp",
      "prompt_id": "abc123",
      "request_text": "What is 2+2?"
    },
    "response": {
      "model": "gemini-2.0-flash-exp",
      "status_code": 200,
      "duration_ms": 1234,
      "input_token_count": 10,
      "output_token_count": 5,
      "total_token_count": 15,
      "response_text": "2+2 equals 4",
      "prompt_id": "abc123",
      "auth_type": "api_key"
    },
    "error": null
  },
  {
    "prompt_id": "def456",
    "request": {
      "model": "gemini-2.0-flash-exp",
      "prompt_id": "def456"
    },
    "response": null,
    "error": {
      "model": "gemini-2.0-flash-exp",
      "error": "Rate limit exceeded",
      "error_type": "rate_limit",
      "status_code": 429,
      "duration_ms": 500,
      "prompt_id": "def456",
      "auth_type": "api_key"
    }
  }
]
```

## Event Types

The script extracts these telemetry events:

- **`gemini_cli.api_request`**: API request attributes (model, prompt_id, request_text)
- **`gemini_cli.api_response`**: API response attributes (status, tokens, response_text)
- **`gemini_cli.api_error`**: API error attributes (error message, error_type, status_code)

Events are matched by their `prompt_id` attribute.

## File Locking

The script uses `filelock` to ensure exclusive access to the log file during processing. If another process is using the log file, you'll see:

```
❌ Error: Could not acquire file lock (timeout after 10s)
   Another process may be using the log file.
   Please try again later or check for running processes.
```

## Telemetry Configuration

Make sure telemetry is enabled in `.gemini/settings.json`:

```json
{
  "telemetry": {
    "enabled": true,
    "target": "local",
    "outfile": ".logging/log.jsonl",
    "logPrompts": true
  }
}
```

## Troubleshooting

### Script won't run
- Make sure `uv` is installed: `pip install uv`
- Check that Python 3.10+ is available

### No events found
- Verify telemetry is enabled in `.gemini/settings.json`
- Check that `.logging/log.jsonl` exists and has content
- Run Gemini CLI with some prompts to generate telemetry

### File lock timeout
- Stop any running `watcher.py` instances
- Close any text editors that may have the log file open
- Wait a few seconds and try again

### Incomplete JSON errors
- This is normal if Gemini is currently writing to the log
- The script handles this gracefully and processes complete records
- Run the script again after Gemini finishes

## Dependencies

- **ijson** (>=3.2.3): Streaming JSON parser for handling large log files efficiently
- **filelock** (>=3.12.0): Cross-platform file locking to prevent concurrent access
- **watchfiles** (>=0.21): Only needed for `watcher.py`

## API Request Viewer

An interactive HTML viewer is available to browse and analyze processed API request logs.

### Opening the Viewer

Simply run the included server script:

```bash
python .logging/server.py
```

The server will:
- ✅ Start a local HTTP server on port 8000
- ✅ Automatically open the viewer in your default browser
- ✅ Serve files with proper CORS headers
- ✅ Handle all file loading without size limits

Press `Ctrl+C` to stop the server when you're done.

**Custom Port:**
```bash
python .logging/server.py 9000  # Use port 9000 instead
```

**Manual Server:**
If you prefer to manage the server manually:
```bash
cd .logging
python -m http.server 8000
# Then open http://localhost:8000/api-viewer.html in your browser
```

### Features

- **📁 File Browser**: Left sidebar lists all `api-requests-*.json` files sorted by date
- **💬 Conversation View**: Shows complete request/response flow with:
  - User messages and prompts
  - Model responses and function calls
  - Function execution results
  - Thought processes (when available)
- **📊 Token Usage**: Displays input/output/cached token counts
- **⏱️ Performance Metrics**: Shows request duration and status codes
- **🎨 Color-Coded Roles**: Easy visual distinction between user, model, and function messages
- **📱 Responsive Design**: Works on desktop, tablet, and mobile

### What's Displayed

For each API request/response pair:

**Request Section:**
- Model name badge
- Complete conversation history
- Function calls with arguments
- Function responses with outputs
- Text content with preserved formatting

**Response Section:**
- HTTP status code
- Response duration (ms)
- Model-generated text
- Token usage breakdown:
  - Input tokens
  - Output tokens
  - Cached tokens
  - Total tokens

**Error Section (if applicable):**
- Error message
- Error type
- Status code

### Tips

- The most recent log file is automatically loaded on page load
- Click any date in the sidebar to switch between different log files
- Function call arguments are displayed in JSON format with syntax highlighting
- Long text content is automatically formatted for readability
- The viewer uses a lightweight HTTP server (no complex setup needed!)
- All request files are stored in the `.logging/requests/` folder
- Server auto-opens your browser when started

## License

Part of the Gemini CLI project.
