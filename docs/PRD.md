# ibe160 Product Requirements Document (PRD)

**Author:** BIP
**Date:** 2025-11-03
**Project Level:** 3
**Target Scale:** 

---

## Goals and Background Context

### Goals

*   Create an engaging, AI-enhanced web-based Beer Game platform for both single-player and multiplayer experiences.
*   Develop a comprehensive classroom management system for educators, featuring automated student allocation, real-time progress tracking, and AI-generated assessments.
*   Ensure the platform is accessible and responsive, providing a seamless experience on desktops and tablets.
*   Leverage AI to provide actionable insights, visualize the bullwhip effect, and enhance learning outcomes.
*   Implement a subscription-based model for educators with secure payment processing.
*   Integrate AI-based players for single-player mode and to fill vacant roles in multiplayer games.

### Background Context

The Beer Game, a simulation from MIT, is a powerful tool for teaching supply chain principles like the bullwhip effect. While existing digital versions exist, they are often expensive, outdated, or lack modern educational features, **specifically the integration of AI**. This project aims to fill that gap by creating an accessible, web-based Beer Game platform that stands out by incorporating AI for opponent simulation, performance analysis, and assessments, aligning with current best practices. It will serve individual learners, students, and professionals by providing an engaging simulation, and will empower educators with a complete classroom management system, making supply chain education more interactive, measurable, and effective.

---

## Requirements

### Functional Requirements

*   **FR001: User Authentication:** The system shall allow users to register and authenticate via email and password.
*   **FR002: Single-Player Game Mode:** The system shall provide a single-player game mode where users can select a role and play with AI-controlled partners.
*   **FR003: Multiplayer Game Mode:** The system shall provide a multiplayer game mode where users can join or host sessions with human or AI-controlled partners.
*   **FR004: Game Configuration:** The system shall allow users to configure game parameters including duration, costs, lead times, difficulty, and communication visibility.
*   **FR005: Interactive Game Dashboard:** The system shall display an interactive, real-time game dashboard showing current inventory, backorders, incoming orders/shipments, week indicator, costs, and an order placement interface.
*   **FR006: AI-Powered Opponents:** The system shall integrate AI (via LLM API) to simulate realistic human decision-making for AI-controlled players.
*   **FR007: Real-time Data Visualization:** The system shall provide real-time data visualizations for inventory levels, orders placed/received, and cost trends.
*   **FR008: AI-Generated Game Summary:** The system shall generate an AI-powered game completion summary including performance metrics, insights, educational content, and bullwhip effect visualization.
*   **FR009: Game State Persistence:** The system shall persist game state to allow users to pause and resume games.
*   **FR010: Teacher Authentication:** The system shall allow teachers to register and authenticate using an institutional email with a manual approval process.
*   **FR011: Subscription Management:** The system shall provide subscription-based access for teachers, including payment processing.
*   **FR012: Class Management:** The system shall allow teachers to create, manage, and configure classes, including bulk student registration and automated/manual game allocation.
*   **FR013: Common Game Settings:** The system shall enforce common game settings for all students within a class to enable comparative analysis.
*   **FR014: Real-time Class Monitoring:** The system shall provide teachers with a real-time monitoring dashboard for active sessions, student progress, and controls to pause/reset games or replace students with AI.
*   **FR015: AI-Generated Assessment System:** The system shall automatically generate tailored assessments (MCQ, short/long text, numeric) for students, with AI-powered grading and feedback.
*   **FR016: Messaging System:** The system shall enable teachers to broadcast messages to a class or send individual messages to students.
*   **FR017: Analytics Dashboard (Educator):** The system shall provide teachers with an analytics dashboard for class-wide metrics, individual reports, bullwhip analysis, and exportable reports.
*   **FR018: Completion Status Management:** The system shall allow teachers to manage and toggle student completion statuses.

### Non-Functional Requirements

*   **NFR001: Performance & Scalability:** The application must load within 3 seconds, with game state updates processing in under 500ms. It must support at least 100 concurrent game sessions without performance degradation, and 95% of database queries must complete within 200ms.
*   **NFR002: Security:** The system must use secure authentication (JWT), enforce data access control with Row Level Security (RLS), encrypt sensitive data, and implement Role-Based Access Control (RBAC). Payment processing must be PCI DSS compliant via Stripe.
*   **NFR003: Reliability & Availability:** The platform must maintain 99% uptime. Game state must be persisted to prevent data loss, and the system must support database backups and disaster recovery.
*   **NFR004: Accessibility:** The user interface must be designed to be accessible to users with disabilities, including those with impaired vision, adhering to WCAG 2.1 AA guidelines.
*   **NFR005: Usability:** The platform must be responsive and fully functional on desktops, laptops, and tablets (minimum 768px width) and compatible with the latest versions of modern browsers (Chrome, Firefox, Safari, Edge).
*   **NFR006: Maintainability:** The codebase must be well-documented, with automated tests covering **100%** of the core game logic to facilitate future development and maintenance.

---

## User Journeys

### Flow 1: Student Playing Single-Player Game

**Entry Point**: Student lands on homepage

1.  **Landing Page**
    *   Student views hero section explaining the Beer Game concept
    *   Reads "How to Play" section with game rules and supply chain structure
    *   Clicks "Start Playing" CTA button

2.  **Authentication**
    *   If not logged in: Redirects to registration/login page
    *   Student registers with email and password
    *   Receives verification email and clicks verification link
    *   Redirected back to platform and automatically logged in

3.  **Game Mode Selection**
    *   Student sees two options:
        *   "Single-Player" (AI opponents)
        *   "Multiplayer" (play with other humans)
    *   Student selects "Single-Player"
    *   Clicks "Continue" button

4.  **Game Configuration**
    *   Student selects their role (Retailer, Wholesaler, Distributor, or Factory)
    *   **Basic Configuration:**
        *   Adjusts game duration using slider (20-52 weeks)
        *   Reviews default cost parameters
    *   **Advanced Configuration (Optional):**
        *   Clicks "Advanced Settings" to expand options
        *   Adjusts cost parameters:
            *   Inventory holding cost per unit per week
            *   Backorder cost per unit per week
            *   Additional costs (transport, lost sales)
        *   Sets lead times (order delay, shipping delay)
        *   Selects difficulty level (easy, medium, hard)
        *   Configures communication/visibility level:
            *   No visibility (default): Can't see other players' inventory
            *   One level: Can see direct upstream/downstream partner's inventory
            *   Two levels: Can see two partners away
            *   Three levels: Full supply chain visibility
    *   Reviews game objectives summary
    *   Clicks "Start Game" button

5.  **Game Dashboard (Week 1-N)**
    *   **View State**:
        *   Current inventory (12 units starting)
        *   Backorders (if any)
        *   Incoming orders from downstream customer
        *   Incoming shipments in transit (2-week delay visualization)
        *   Week indicator (e.g., "Week 1 of 20")
        *   Real-time cost accumulation display (inventory + backorder + other costs)
    *   **View Visibility (based on configuration)**:
        *   If visibility enabled: Shows inventory/backorder levels of other supply chain positions
        *   If no visibility: Only shows own position
    *   **Make Decision**: Student enters order quantity in input field
    *   **Validate**: System validates order (positive integer, reasonable bounds)
    *   **Submit**: Student clicks "Place Order" button
    *   **Processing**: System advances to next week:
        *   AI players make their decisions via LLM API calls
        *   System calculates inventory changes, backorders, and costs
        *   Updates all supply chain positions
        *   Updates charts and visualizations
    *   **Repeat**: Student continues for configured number of weeks

6.  **Real-Time Monitoring (During Game)**
    *   Student views live charts updating each week:
        *   Own inventory levels over time
        *   Orders placed and received timeline
        *   Cumulative cost trends (broken down by cost type if advanced costs enabled)
    *   If visibility enabled: Can see other players' inventory trends
    *   Student observes cost accumulation in real-time

7.  **Game Completion**
    *   After final week, AI generates comprehensive summary dashboard:
        *   **Performance Metrics:**
            *   Total costs breakdown by category (inventory, backorder, transport, lost sales)
            *   Final inventory levels
            *   Total backorders experienced
            *   Peak inventory/backorder weeks
        *   **Comparison with Benchmarks:**
            *   Comparison with optimal performance (best possible cost)
            *   Comparison with typical player performance
        *   **AI-Generated Insights:**
            *   Key insights about decisions (e.g., "You over-ordered in weeks 5-8, causing excess inventory of 45 units and $225 in holding costs")
            *   Identification of decision patterns (reactive vs. proactive ordering)
            *   Analysis of how player contributed to/mitigated bullwhip effect
        *   **Educational Content:**
            *   Explanation of supply chain phenomena observed in this game
            *   Bullwhip effect visualization showing demand amplification across supply chain
            *   Recommended strategies for improvement
    *   Student has options:
        *   "Play Again" - returns to game configuration
        *   "Try Different Role" - returns to configuration with new role
        *   "View Detailed Analytics" - expands full game history
        *   "Exit to Dashboard" - returns to user dashboard

**Exit Point**: Student returns to main dashboard or logs out

---

### Flow 2: Teacher Setting Up Class Game

**Entry Point**: Teacher lands on homepage

1.  **Landing Page**
    *   Teacher clicks "For Educators" button in navigation
    *   Views educator features and pricing information

2.  **Teacher Registration & Subscription**
    *   Clicks "Get Started" button
    *   Registers with institutional email address
    *   Redirected to subscription selection page
    *   Selects plan (Basic $19/month, Professional $39/month, or Institution $99/month)
    *   Clicks "Start Free Trial" (14 days)
    *   Redirected to Stripe Checkout page
    *   Enters payment information
    *   Returns to platform after payment setup

3.  **Teacher Dashboard Access**
    *   Lands on teacher dashboard showing:
        *   List of classes (empty for new teacher)
        *   "Create New Class" button prominently displayed
        *   Navigation to Monitoring, Analytics, Settings

4.  **Create Class**
    *   Clicks "Create New Class" button
    *   Enters class information:
        *   Class name (e.g., "Supply Chain Management 101 - Fall 2024")
        *   Academic year/semester
    *   Clicks "Create Class"
    *   Redirected to class detail page

5.  **Add Students**
    *   Teacher has two options:
        *   **Option A - Bulk Import**: Clicks "Import Students" button
            *   Downloads CSV template
            *   Fills in student names and emails
            *   Uploads CSV file
            *   System validates and imports students
            *   Sends registration emails to all students
        *   **Option B - Manual Entry**: Clicks "Add Student" button
            *   Enters student name and email
            *   Repeats for each student
            *   System sends registration invitation

6.  **Configure Game Session (Common Settings for All Students)**
    *   Clicks "Create Game Assignment" button
    *   **Common Configuration Applied to All Games in Class:**
        *   Game duration (20-52 weeks) - same for all students
        *   **Cost parameters** (same for all):
            *   Inventory holding cost per unit per week
            *   Backorder cost per unit per week
            *   Additional costs (transport, lost sales)
        *   **Lead times** (same for all):
            *   Order processing delay
            *   Shipping delay
        *   Difficulty level (easy, medium, hard) - affects demand variability
        *   **External demand pattern** - same customer demand across all games
        *   **Communication/visibility level:**
            *   No visibility, one level, two levels, or three levels
    *   **Rationale displayed:** "All games will use identical settings to enable fair performance comparison across students"
    *   Sets allocation preferences:
        *   Students per game (1-4)
        *   Random allocation or manual assignment option
    *   Clicks "Auto-Allocate Students"
    *   System automatically distributes students to game sessions
    *   **Manual override option:** Teacher can drag-and-drop students to different games if needed

7.  **Review Allocation**
    *   Views allocation summary showing:
        *   Number of game sessions created
        *   Students assigned to each session with their roles
        *   AI-controlled positions highlighted
        *   Common game configuration summary displayed at top
    *   Can manually adjust assignments if needed
    *   Clicks "Activate Games" button
    *   Students receive notification emails with game instructions

8.  **Monitor Progress (Enhanced Controls)**
    *   Teacher navigates to "Monitoring" dashboard
    *   Views table of all active game sessions with columns:
        *   Game ID / Session name
        *   Game status (not started, in progress, paused, completed)
        *   Current week for each game
        *   Student names and roles
        *   Real-time cost data for each student
        *   Completion status toggle
    *   **Class-wide controls:**
        *   "Pause All Games" button - freezes all games simultaneously
        *   "Resume All Games" button - restarts all paused games
        *   "Reset All Games" button - resets all games to week 1 (with confirmation)
    *   **Individual game actions:**
        *   Clicks on specific game to see detailed real-time view:
            *   Week-by-week progress
            *   Individual student decisions and order history
            *   Supply chain visualizations
        *   "Remove Student" button - removes a student from a game
            *   System automatically replaces student with AI player
            *   Original student's data archived for reference
    *   Toggle completion status for each student (approved/not approved)

9.  **Send Messages to Students**
    *   From monitoring dashboard, teacher clicks "Messages" button
    *   Two options:
        *   **Broadcast to All Students:**
            *   Clicks "Message All Students" button
            *   Composes message in text editor
            *   Optional: Attach files (PDFs, instructions)
            *   Clicks "Send to All" button
            *   All students in class receive email + in-app notification
        *   **Message Individual Student:**
            *   Clicks message icon next to specific student
            *   Composes personalized message
            *   Clicks "Send" button
            *   Student receives email + in-app notification

10. **Generate Assessments (Multiple Question Types)**
    *   After students complete games, teacher clicks "Generate Assessments"
    *   System uses AI to create custom assessment for each student:
        *   Questions based on specific events in that student's game session
        *   Covers concepts like bullwhip effect, inventory management, ordering strategies
    *   **Question types generated:**
        *   **Multiple choice:** 4 options, AI-generated, auto-graded
        *   **Short text answer:** Brief explanation required, AI-assessed
        *   **Long text answer:** Detailed analysis required, AI-assessed
        *   **Numeric answer:** Calculation-based, auto-graded
    *   **AI assigns weights** to each question based on difficulty
    *   **Teacher sets passing threshold:**
        *   Enters minimum score percentage (e.g., 70%)
        *   Students must meet threshold to be marked as "approved"
    *   Teacher reviews and can edit generated questions
    *   Teacher clicks "Approve and Send Assessments"
    *   Students receive assessment notification

11. **View Analytics**
    *   Teacher navigates to "Analytics" dashboard
    *   Views class-wide metrics:
        *   Average total costs by game session (comparable since all use same settings)
        *   Bullwhip effect analysis across all games
        *   Common decision patterns and mistakes
        *   Individual student performance rankings
        *   Distribution of costs by type (inventory, backorder, transport, lost sales)
    *   **Comparative analysis enabled by common configuration:**
        *   Fair comparison of student performance
        *   Identification of best-performing students
        *   Analysis of role-specific challenges
    *   Applies filters (by game session, by role, by time period)
    *   Clicks "Export Report" button
    *   Selects format (PDF for presentation, CSV for further analysis)
    *   Downloads comprehensive class report

**Exit Point**: Teacher logs out or navigates to other classes

---

### Flow 3: Student Completing Assessment (Multiple Question Types)

**Entry Point**: Student receives email notification about assessment

1.  **Email Notification**
    *   Student receives email: "Your Beer Game assessment is ready"
    *   Clicks link in email
    *   Redirected to login page (if not logged in)

2.  **Assessment Dashboard**
    *   Student lands on assessment page showing:
        *   Game summary (their role, total cost, final week)
        *   Number of questions (typically 8-12 questions of mixed types)
        *   Weighted scoring explanation: "Questions are weighted by difficulty"
        *   Passing threshold displayed (e.g., "You need 70% to pass")
        *   Time estimate (20-30 minutes)
    *   Clicks "Start Assessment" button

3.  **Answer Questions (Multiple Types)**
    *   **For Multiple Choice Questions:**
        *   Student reads question (e.g., "In week 8, you placed an order for 20 units despite having 15 units in inventory. What likely caused your backlog in week 12?")
        *   Views 4 multiple-choice options (A, B, C, D)
        *   Selects one answer by clicking radio button
        *   Question weight displayed (e.g., "Weight: 1.5x")
        *   Clicks "Next Question"

    *   **For Short Text Answer Questions:**
        *   Student reads question (e.g., "Briefly explain why your inventory peaked in week 12.")
        *   Text input field with character limit (100-200 characters)
        *   Placeholder: "Enter your answer in 2-3 sentences"
        *   Question weight displayed (e.g., "Weight: 2x")
        *   Clicks "Next Question"

    *   **For Long Text Answer Questions:**
        *   Student reads question (e.g., "Analyze your ordering strategy throughout the game. How did your decisions contribute to or mitigate the bullwhip effect?")
        *   Large text area with character limit (300-500 characters)
        *   Placeholder: "Provide a detailed analysis with specific examples from your game"
        *   Question weight displayed (e.g., "Weight: 3x")
        *   Clicks "Next Question"

    *   **For Numeric Answer Questions:**
        *   Student reads question (e.g., "Calculate the total inventory holding cost you incurred in weeks 5-10.")
        *   Number input field
        *   Units displayed (e.g., "dollars")
        *   Question weight displayed (e.g., "Weight: 1x")
        *   Clicks "Next Question"

    *   Progress indicator shows questions completed (e.g., "Question 5 of 10")
    *   Can navigate back to previous questions before final submission

4.  **Submit Assessment**
    *   After final question, student clicks "Submit Assessment"
    *   Confirmation modal: "Are you sure you want to submit? You cannot change answers after submission."
    *   Student confirms submission
    *   System processes:
        *   Auto-grades multiple choice and numeric questions
        *   Sends text answers to AI for assessment
        *   Calculates weighted score

5.  **Immediate Feedback (AI-Generated)**
    *   System shows results page:
        *   **Overall weighted score** (e.g., "78.5% - PASSED" in green or "65.0% - NOT PASSED" in red)
        *   Passing threshold reminder (e.g., "Passing threshold: 70%")
        *   **Question-by-question breakdown:**
            *   Question number and type
            *   Question weight
            *   Points earned / points possible
            *   Student's answer displayed
            *   For multiple choice/numeric: Correct answer shown if wrong
            *   **AI-generated explanation for each question:**
                *   Example for wrong MC: "Your answer was incorrect. The backlog was caused by underestimating the 2-week shipping delay in weeks 6-8. When you finally increased orders in week 8, it was too late to prevent stockouts."
                *   Example for text answer: "Your analysis correctly identified the reactive ordering pattern. However, you could have discussed how this contributed to the bullwhip effect in more detail. Score: 7/10"
                *   Example for numeric: "Correct! The total inventory holding cost was $450 (90 units × $0.50/unit/week × 10 weeks)."
    *   Student can review game data alongside feedback
    *   Link to detailed game replay for context

6.  **Approval Status Update**
    *   If student passed (score ≥ threshold):
        *   Status automatically updated to "Approved"
        *   Congratulatory message displayed
        *   Option to download certificate
    *   If student failed (score < threshold):
        *   Status remains "Not Approved"
        *   Message: "Please review the feedback and discuss with your teacher"
        *   Teacher notified of student's score

7.  **Download Certificate (If Passed)**
    *   Student clicks "Download Certificate" button
    *   Receives PDF certificate showing:
        *   Game completion
        *   Assessment score
        *   Date completed
        *   Teacher's signature (digital)

**Exit Point**: Student returns to dashboard or logs out

---

### Flow 4: Individual Learner (Non-Student) Quick Play

**Entry Point**: Professional/learner finds site via search or recommendation

1.  **Landing Page**
    *   Visitor views hero section with game demo video
    *   Reads about learning objectives (bullwhip effect, systems thinking)
    *   Clicks "Play Free Demo" button (no registration required)

2.  **Quick Game Setup**
    *   Guest selects role from 4 supply chain positions
    *   System auto-configures 20-week game with standard parameters
    *   No customization options (keeps it simple)
    *   Clicks "Start Demo Game"

3.  **Demo Gameplay**
    *   Plays abbreviated Beer Game (same dashboard as registered students)
    *   Full functionality including:
        *   Real-time charts
        *   AI opponents
        *   Cost tracking
    *   Game state not saved (session-only)

4.  **Game End - Conversion Prompt**
    *   Views performance summary
    *   System shows upsell prompt:
        *   "Create free account to save games and track progress"
        *   "Compare your performance with other players"
    *   Options:
        *   "Create Free Account" - goes to registration
        *   "Play Again as Guest" - returns to quick setup
        *   "Maybe Later" - returns to landing page

5.  **Optional Registration**
    *   If user clicks "Create Free Account":
        *   Quick registration form (email + password)
        *   Email verification
        *   Game history retroactively saved
        *   Access to full features (multiple games, strategy comparison)

**Exit Point**: User closes browser or creates account and enters main platform

---

### Flow 5: Teacher Managing Subscription

**Entry Point**: Teacher logged into dashboard

1.  **Access Subscription Settings**
    *   Teacher clicks profile icon in top-right
    *   Selects "Subscription & Billing" from dropdown menu
    *   Lands on subscription management page

2.  **View Current Status**
    *   Page displays:
        *   Current plan (e.g., "Professional - $39/month")
        *   Student usage (e.g., "42 of 150 students")
        *   Next billing date
        *   Payment method (last 4 digits of card)

3.  **Upgrade/Downgrade Plan**
    *   Teacher clicks "Change Plan" button
    *   Views comparison table of all three plans
    *   Selects new plan (e.g., upgrade from Basic to Professional)
    *   System shows prorated cost adjustment
    *   Clicks "Confirm Change"
    *   Stripe processes change immediately
    *   New limits applied to account

4.  **Update Payment Method**
    *   Teacher clicks "Update Payment Method"
    *   Redirected to Stripe Customer Portal
    *   Updates card information
    *   Returns to platform
    *   Confirmation message displayed

5.  **View Invoices**
    *   Teacher clicks "Invoice History" tab
    *   Views list of all past payments
    *   Can download any invoice as PDF
    *   Useful for expense reports and reimbursement

6.  **Cancel Subscription (Edge Case)**
    *   Teacher clicks "Cancel Subscription" link (bottom of page)
    *   System shows warning:
        *   "Your students will lose access at end of billing period"
        *   "All class data will be archived but not deleted"
    *   Teacher confirms cancellation
    *   Account remains active until billing period ends
    *   Receives confirmation email with final access date

**Exit Point**: Teacher returns to main dashboard

---

### Flow 6: Student Playing Multiplayer Game

**Entry Point**: Student wants to play with other human players

1.  **Landing Page / Dashboard**
    *   Student clicks "Start Playing" button
    *   Proceeds through authentication (if needed)

2.  **Game Mode Selection**
    *   Student sees two options:
        *   "Single-Player" (AI opponents)
        *   "Multiplayer" (play with other humans)
    *   Student selects "Multiplayer"
    *   Clicks "Continue" button

3.  **Multiplayer Lobby Options**
    *   Student sees two paths:
        *   **Create New Game**: "Host a new game session"
        *   **Join Existing Game**: "Join a game waiting for players"
    *   Student chooses one path

4a. **Path A: Create New Game (Host)**
    *   Student clicks "Create New Game"
    *   Configures game parameters:
        *   Game duration (20-52 weeks)
        *   Basic or advanced cost parameters
        *   Lead times
        *   Difficulty level
        *   Communication/visibility level
    *   Selects their preferred role (Retailer, Wholesaler, Distributor, or Factory)
    *   Sets game visibility:
        *   Public: Anyone can join
        *   Private: Share invite code with specific players
    *   Clicks "Create Game Room"
    *   System generates unique game room code (e.g., "BEER-A3K9")
    *   Student enters waiting lobby

5a. **Waiting Lobby (Host Perspective)**
    *   Displays game room code prominently
    *   "Share" button to copy invite link
    *   Shows 4 supply chain positions with status:
        *   Retailer: [Host's name] ✓
        *   Wholesaler: Waiting for player...
        *   Distributor: Waiting for player...
        *   Factory: Waiting for player...
    *   Real-time updates as players join
    *   Host gets a notification when a player joins
    *   Host controls:
        *   "Start Game with AI" button - fills empty positions with AI and starts
        *   "Cancel Game" button - disbands the room
    *   Chat window for players to communicate before game starts

4b. **Path B: Join Existing Game (Joiner)**
    *   Student clicks "Join Existing Game"
    *   Two options:
        *   Enter game room code manually
        *   Browse list of public games waiting for players
    *   If browsing:
        *   Sees list of available games with:
            *   Host name
            *   Game duration
            *   Available positions
            *   Number of human players already joined (e.g., "2/4 players")
        *   Filters: Duration, difficulty level
    *   Student selects a game or enters code
    *   Clicks "Join Game"

5b. **Waiting Lobby (Joiner Perspective)**
    *   Sees game configuration (read-only)
    *   Selects available role from remaining positions
    *   Sees other players who have joined
    *   Chat window to communicate with other players
    *   "Leave Game" button if they change their mind
    *   Waits for host to start game or for all 4 positions to fill

6.  **Game Start Trigger**
    *   **Option 1:** Host clicks "Start Game with AI" - fills empty slots with AI
    *   **Option 2:** All 4 positions filled by humans - game auto-starts after 10-second countdown
    *   All players receive notification: "Game starting in 10... 9... 8..."

7.  **Multiplayer Game Dashboard (Week 1-N)**
    *   **Turn-based gameplay:**
        *   All players see "Week X - Waiting for all players to submit orders"
        *   Each player's own order input is active
        *   Other players' order inputs show "Waiting..." status
        *   Real-time indicator shows who has submitted (e.g., "3/4 players submitted")
    *   **View State** (same as single-player):
        *   Current inventory
        *   Backorders
        *   Incoming orders
        *   Incoming shipments
        *   Cost accumulation
    *   **Visibility based on configuration:**
        *   If visibility enabled: Can see other players' inventory levels in real-time
        *   If not: Only see own position
    *   **Player presence indicators:**
        *   Green dot next to active players
        *   Gray dot if player disconnected (host can choose to let AI take over temporarily)
    *   **Make Decision:**
        *   Player enters order quantity
        *   Clicks "Submit Order"
        *   Status changes to "Waiting for other players..."
    *   **Week Advancement:**
        *   Once all 4 players submit orders, week auto-advances
        *   If player inactive for 5 minutes, the host can decide to let AI make decision for them (warning shown)
    *   **Optional in-game features:**
        *   Quick chat messages (if enabled): Predefined messages like "Order spike incoming!"
        *   Player can see other players' names and roles

8.  **Game Completion (Multiplayer)**
    *   After final week, all players see summary dashboard simultaneously
    *   **Performance Comparison:**
        *   Side-by-side costs for all 4 players
        *   Individual rankings based on deviation from expected performance with given role (1st, 2nd, 3rd, 4th place)
        *   Total supply chain cost (sum of all 4 players)
    *   **AI-Generated Insights** (personalized for each player):
        *   Individual analysis of decisions
        *   How player's decisions impacted other players
        *   Contribution to bullwhip effect
    *   **Supply Chain Performance:**
        *   Bullwhip effect visualization showing all 4 positions
        *   Analysis of team coordination (or lack thereof)
    *   **Social Features:**
        *   Option to send congratulations to other players
        *   "Play Again" button - starts new game with same players
    *   Each player can download their own game report

**Exit Point**: Player returns to dashboard or starts new multiplayer game

---

## UX Design Principles

*   **Clarity and Intuitiveness:** The interface should be clean and easy to understand, allowing players to focus on the simulation rather than navigating a complex UI. Key data (inventory, orders, costs) must be instantly recognizable.
*   **Informative Feedback:** The system must provide immediate and clear feedback on player actions, game state changes, and performance, helping users understand the consequences of their decisions in real-time.
*   **Educational Focus:** Every design element should support the primary goal of learning. Visualizations and AI-generated insights must be presented in a way that is easy to digest and directly relates to supply chain concepts.
*   **Efficiency for Educators:** The teacher dashboard must be designed for efficiency, enabling educators to manage classes, monitor progress, and generate assessments with minimal clicks and a clear, logical workflow.

---

## User Interface Design Goals

*   **Platform & Screens:** The primary platform is a responsive web application for desktops, laptops, and tablets. Key screens include: the main game dashboard, the teacher's class management and monitoring views, the assessment interface, and the analytics/summary pages.
*   **Visual Style:** The design should be modern, professional, and data-driven. It will use a clean layout with a clear visual hierarchy. Data visualizations (charts, graphs) are central and must be interactive and easy to read.
*   **Key Interactions:** Core interactions involve placing orders via a simple input, navigating weekly rounds, and exploring interactive charts. For educators, key interactions include bulk student import, drag-and-drop for manual allocation, and one-click game controls (pause/reset).
*   **Design Constraints:** The design must adhere to accessibility (WCAG 2.1 AA) guidelines. It should be implemented using a component-based architecture (e.g., with Shadcn UI and Tailwind CSS) to ensure consistency and maintainability.

---

## Epic List

*   **Epic 1: Project Foundation & Core Game Engine:** Establishes the technical foundation (repo, CI/CD, DB schema), implements user authentication, and builds the core single-player game logic with AI opponents and state persistence.
*   **Epic 2: Interactive Game Dashboard & Visualizations:** Develops the complete player-facing UI, including the real-time dashboard, interactive charts for inventory and costs, and the AI-generated game summary screen.
*   **Epic 3: Educator Platform & Class Management:** Implements teacher registration, subscription management (via Stripe), and the core class management dashboard, including creating classes and managing student enrollment (bulk and manual).
*   **Epic 4: Advanced Classroom & Game Administration:** Builds the real-time monitoring dashboard for teachers, including controls to pause/reset games, replace students with AI, and the class-wide messaging system.
*   **Epic 5: AI-Powered Assessment & Analytics:** Develops the AI-driven assessment generation system (all question types), the automated grading/feedback flow, and the comprehensive analytics dashboard for educators with export functionality.
*   **Epic 6: Multiplayer Game Mode:** Implements the multiplayer functionality, including creating and joining public/private game rooms, the waiting lobby, and the turn-based gameplay synchronization.

> **Note:** Detailed epic breakdown with full story specifications is available in [epics.md](./epics.md)

---

## Out of Scope

*   **In-game chat:** While desirable for multiplayer, real-time in-game chat will be deferred to a future phase to focus on core gameplay and educational features.
*   **Advanced customization options:** Features like variable demand patterns, custom cost parameters beyond the initial set, different product types, and custom supply chain configurations will be considered for future enhancements.
*   **Gamification features:** Leaderboards, achievement badges, and performance levels are planned for later iterations to enhance engagement after the core platform is stable.
*   **Advanced analytics:** Predictive performance indicators, decision pattern analysis, and comparative benchmarking against historical data will be explored in future phases.
*   **Mobile app:** A dedicated iOS/Android mobile application for game participation is a future consideration; the MVP will focus on a responsive web-based experience.
*   **LMS integration:** Direct integration with Learning Management Systems (e.g., Canvas, Moodle) will be considered post-MVP based on user demand.
*   **Social sharing features:** Sharing game results or achievements on social media platforms is out of scope for the initial release.
*   **Replay and strategy analysis tools:** Advanced tools for replaying game sessions and in-depth strategy analysis will be developed in subsequent phases.
*   **Collaborative team mode:** The ability for multiple students to manage one supply chain position is a future enhancement.
*   **Multilingual support:** The initial release will support English only; multilingual support will be added based on market demand.
