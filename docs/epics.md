# ibe160 Epics & Stories

**Author:** BIP
**Date:** 2025-11-03
**Project Level:** 4

---

This document provides the detailed story breakdown for each epic defined in the [PRD.md](./PRD.md). It serves as the tactical implementation roadmap.

---

## Epic 1: Project Foundation & Core Game Engine

**Goal:** Establish the technical foundation (repo, CI/CD, DB schema), implement user authentication, and build the core single-player game logic with AI opponents and state persistence.

---

**Story 1.1: Project & CI/CD Setup**

*   **As a** Developer,
*   **I want** to set up the Git repository, Next.js frontend, and FastAPI backend projects,
*   **So that** we have a version-controlled codebase.

**Acceptance Criteria:**
1.  A monorepo is created containing both frontend and backend projects.
2.  Basic CI/CD pipelines are configured in Vercel to auto-deploy the `main` branch.
3.  A `README.md` file is created with setup instructions.

---

**Story 1.2: Database Schema & Migrations**

*   **As a** Developer,
*   **I want** to define and implement the initial database schema using SQLAlchemy and Alembic,
*   **So that** we can store all required application data.

**Acceptance Criteria:**
1.  Alembic is configured for database migrations.
2.  Initial migration script creates all tables defined in the `proposal.md` (Users, Games, Players, Game Rounds, etc.).
3.  Relationships between tables are correctly defined with foreign keys.

---

**Story 1.3: User Registration & Authentication**

*   **As a** User,
*   **I want** to register for a new account using my email and password and log in,
*   **So that** I can access the platform.

**Acceptance Criteria:**
1.  A user can register on a dedicated registration page.
2.  The system sends a verification email upon registration.
3.  A user cannot log in until their email is verified.
4.  A registered user can log in successfully and receive a JWT token.
5.  Supabase RLS is enabled for basic data protection.

---

**Story 1.4: Core Game State Machine**

*   **As a** Player,
*   **I want** the game to accurately process weekly turns,
*   **So that** inventory, orders, and costs are calculated correctly according to the rules.

**Acceptance Criteria:**
1.  A state machine correctly processes the sequence of events each week (receive shipment, update inventory, receive order, place order).
2.  Inventory holding costs and backorder costs are calculated accurately at the end of each week.
3.  The game state is correctly updated and ready for the next turn.

---

**Story 1.5: AI Player Integration**

*   **As a** Player,
*   **I want** to play against AI opponents that make realistic decisions,
*   **So that** the single-player mode is engaging.

**Acceptance Criteria:**
1.  The system can call the Gemini API to get an order decision for an AI-controlled player.
2.  The AI is provided with the necessary context (current game state, role, rules) to make a decision.
3.  The AI's order is successfully integrated into the game's turn processing.
4.  A fallback mechanism (e.g., simple rule-based logic) is in place in case the API call fails.

---

**Story 1.6: Game State Persistence**

*   **As a** Player,
*   **I want** my game progress to be saved automatically each week,
*   **So that** I can pause and resume my game later.

**Acceptance Criteria:**
1.  The complete state of a game is saved to the database at the end of each week.
2.  A user can see a list of their active games on their dashboard.
3.  A user can resume an active game, and it will load to the correct week with the correct state.

---

## Epic 2: Interactive Game Dashboard & Visualizations

**Goal:** Develop the complete player-facing UI, including the real-time dashboard, interactive charts for inventory and costs, and the AI-generated game summary screen.

---

**Story 2.1: Game Setup UI**

*   **As a** Player,
*   **I want** a user-friendly interface to create and configure a new game,
*   **So that** I can easily set up a single-player or multiplayer session.

**Acceptance Criteria:**
1.  A user can select their desired role (Retailer, Wholesaler, etc.).
2.  A user can configure game parameters (duration, costs, lead times) using intuitive controls (sliders, inputs).
3.  Advanced configuration options can be expanded or collapsed.
4.  The UI clearly distinguishes between single-player and multiplayer setup.

---

**Story 2.2: Real-Time Game Dashboard UI**

*   **As a** Player,
*   **I want** to see all critical game information on a single screen,
*   **So that** I can make informed decisions each week.

**Acceptance Criteria:**
1.  The dashboard clearly displays current inventory, backorders, incoming shipments, and incoming orders.
2.  The current week and total costs are prominently displayed.
3.  The order input field is easy to use and includes validation.
4.  The UI updates in real-time as the game progresses to the next week.

---

**Story 2.3: Live Data Visualization**

*   **As a** Player,
*   **I want** to view live charts of my performance,
*   **So that** I can understand trends and the consequences of my actions.

**Acceptance Criteria:**
1.  A line chart displays the player's inventory and backorder levels over time, updating each week.
2.  A bar or line chart displays the orders placed and received over time.
3.  A chart shows the cumulative costs, broken down by type (inventory vs. backorder).
4.  Charts are interactive (e.g., tooltips showing values on hover).

---

**Story 2.4: AI-Generated Game Summary UI**

*   **As a** Player,
*   **I want** to view a comprehensive and visually appealing summary after completing a game,
*   **So that** I can understand my performance and learn from it.

**Acceptance Criteria:**
1.  The summary page displays final performance metrics (total cost, etc.).
2.  AI-generated insights and educational content are clearly presented.
3.  A final visualization clearly illustrates the bullwhip effect across the supply chain.
4.  The UI includes options to "Play Again" or "Exit to Dashboard".

---

## Epic 3: Educator Platform & Class Management

**Goal:** Implement teacher registration, subscription management (via Stripe), and the core class management dashboard, including creating classes and managing student enrollment (bulk and manual).

---

**Story 3.1: Teacher Registration & Authentication**

*   **As a** Teacher,
*   **I want** to register and log in using my institutional email,
*   **So that** I can access the educator features.

**Acceptance Criteria:**
1.  A teacher can register with an institutional email address.
2.  Email verification is required for teacher accounts.
3.  Successful login grants access to the teacher dashboard.
4.  Teacher role is correctly assigned and enforced via RLS.

---

**Story 3.2: Subscription Management Integration**

*   **As a** Teacher,
*   **I want** to select a subscription plan and manage my billing,
*   **So that** I can access class management features.

**Acceptance Criteria:**
1.  Teachers can select from defined subscription plans (Basic, Professional, Institution).
2.  Stripe Checkout is integrated for secure payment processing.
3.  Stripe webhooks are configured to update subscription status in the database.
4.  Teachers can view their current plan, billing date, and payment method.

---

**Story 3.3: Class Creation & Management**

*   **As a** Teacher,
*   **I want** to create and manage multiple classes,
*   **So that** I can organize my students and game assignments.

**Acceptance Criteria:**
1.  A teacher can create a new class by providing a name and academic year.
2.  A teacher can view a list of their created classes.
3.  A teacher can edit or delete existing classes (with confirmation).

---

**Story 3.4: Bulk Student Import**

*   **As a** Teacher,
*   **I want** to import multiple students at once using a CSV file,
*   **So that** I can efficiently populate my classes.

**Acceptance Criteria:**
1.  A teacher can download a CSV template for student import.
2.  The system can parse a CSV file containing student names and emails.
3.  Students are automatically registered (if new) and enrolled in the class.
4.  Registration invitation emails are sent to imported students.

---

**Story 3.5: Manual Student Enrollment**

*   **As a** Teacher,
*   **I want** to manually add individual students to a class,
*   **So that** I can manage enrollment flexibly.

**Acceptance Criteria:**
1.  A teacher can add a student by entering their name and email.
2.  The system sends a registration invitation to the manually added student.
3.  A teacher can remove a student from a class.

---

**Story 3.6: Common Game Configuration for Classes**

*   **As a** Teacher,
*   **I want** to set common game parameters for all games within a class,
*   **So that** student performance can be fairly compared.

**Acceptance Criteria:**
1.  A teacher can configure game duration, costs, lead times, difficulty, and communication visibility for a class.
2.  All game sessions created for that class automatically inherit these common settings.
3.  The UI clearly indicates that these settings apply class-wide.

---

## Epic 4: Advanced Classroom & Game Administration

**Goal:** Builds the real-time monitoring dashboard for teachers, including controls to pause/reset games, replace students with AI, and the class-wide messaging system.

---

**Story 4.1: Real-Time Monitoring Dashboard**

*   **As a** Teacher,
*   **I want** to view a real-time dashboard of all active game sessions in my class,
*   **So that** I can monitor student progress and identify issues.

**Acceptance Criteria:**
1.  The dashboard displays a table of all active games.
2.  Each row shows the game status (in progress, paused), current week, and student names/roles.
3.  Key performance metrics (e.g., total cost) are displayed for each student and updated in real-time.
4.  A teacher can click on a specific game to view a detailed real-time visualization of that game's supply chain.

---

**Story 4.2: Game Control Actions (Pause/Reset)**

*   **As a** Teacher,
*   **I want** to be able to pause, resume, or reset games for the entire class or for individual sessions,
*   **So that** I can manage the classroom experience effectively.

**Acceptance Criteria:**
1.  A "Pause All Games" button freezes all active sessions in the class.
2.  A "Resume All Games" button unpauses all paused sessions.
3.  A "Reset All Games" button resets all games to week 1 (requires confirmation).
4.  Individual games can be paused, resumed, or reset from the monitoring dashboard.

---

**Story 4.3: AI Student Replacement**

*   **As a** Teacher,
*   **I want** to be able to remove a student from an active game and have an AI player take over,
*   **So that** the game can continue without disruption if a student is absent.

**Acceptance Criteria:**
1.  A teacher can remove a student from an active game session via the monitoring dashboard.
2.  The system automatically replaces the removed student with an AI-controlled player.
3.  The AI player takes over from the current week, using the game state left by the student.
4.  The original student's data is archived for assessment purposes.

---

**Story 4.4: Class Messaging System**

*   **As a** Teacher,
*   **I want** to send messages to all students in a class or to individual students,
*   **So that** I can provide instructions, hints, or feedback.

**Acceptance Criteria:**
1.  A teacher can broadcast a message that is sent to every student in the class.
2.  A teacher can send a private message to an individual student.
3.  Students receive messages as in-app notifications and/or emails.
4.  The system allows for attaching files (e.g., PDF instructions) to broadcast messages.

---

## Epic 5: AI-Powered Assessment & Analytics

**Goal:** Develops the AI-driven assessment generation system (all question types), the automated grading/feedback flow, and the comprehensive analytics dashboard for educators with export functionality.

---

**Story 5.1: AI-Generated Assessment Creation**

*   **As a** Teacher,
*   **I want** the system to automatically generate a tailored assessment for each student based on their individual game performance,
*   **So that** I can accurately evaluate their understanding of supply chain concepts.

**Acceptance Criteria:**
1.  The system generates a mix of question types (Multiple Choice, Short Answer, Numeric) based on events from a student's specific game.
2.  The AI assigns a difficulty weight to each question.
3.  A teacher can set a passing threshold for the assessment.
4.  A teacher can review, edit, or delete any AI-generated question before sending the assessment to students.

---

**Story 5.2: Student Assessment Interface**

*   **As a** Student,
*   **I want** a clear and intuitive interface to complete my post-game assessment,
*   **So that** I can demonstrate what I have learned.

**Acceptance Criteria:**
1.  The interface presents one question at a time with clear instructions.
2.  A progress indicator shows the student how many questions are left.
3.  Students can navigate back to previous questions to review or change answers before final submission.
4.  The interface is responsive and works on desktops and tablets.

---

**Story 5.3: Automated Grading and Feedback**

*   **As a** Student,
*   **I want** to receive immediate, detailed feedback after submitting my assessment,
*   **So that** I can understand my mistakes and learn from them.

**Acceptance Criteria:**
1.  Multiple choice and numeric questions are auto-graded instantly.
2.  Short text answers are assessed by an AI, which provides a score and qualitative feedback.
3.  The final weighted score is calculated and displayed immediately.
4.  For each incorrect answer, the system provides an AI-generated explanation of the correct answer, referencing events from the student's game.

---

**Story 5.4: Educator Analytics Dashboard**

*   **As a** Teacher,
*   **I want** to view a comprehensive analytics dashboard for my class,
*   **So that** I can analyze class-wide performance and identify trends.

**Acceptance Criteria:**
1.  The dashboard displays class-wide metrics, such as average costs and bullwhip effect analysis.
2.  A teacher can view and compare the performance of individual students.
3.  Visualizations clearly show performance distributions and identify common mistakes across the class.
4.  A teacher can filter the data by game session, student role, or date.

---

**Story 5.5: Data Export Functionality**

*   **As a** Teacher,
*   **I want** to be able to export the class analytics report,
*   **So that** I can use the data for grading, research, or sharing with colleagues.

**Acceptance Criteria:**
1.  A teacher can export the full class analytics report as a PDF file.
2.  A teacher can export the raw performance data as a CSV file for further analysis.
3.  The exported reports are well-formatted and easy to read.

---

## Epic 6: Multiplayer Game Mode

**Goal:** Implements the multiplayer functionality, including creating and joining public/private game rooms, the waiting lobby, and the turn-based gameplay synchronization.

---

**Story 6.1: Create/Join Game Room**

*   **As a** Player,
*   **I want** to be able to host a new multiplayer game or join an existing one,
*   **So that** I can play with other human players.

**Acceptance Criteria:**
1.  A player can create a new game and set it to public or private (invite-only).
2.  A unique, shareable game code is generated for private games.
3.  A player can browse and join a list of public games that are waiting for players.
4.  A player can join a private game by entering the game code.

---

**Story 6.2: Multiplayer Waiting Lobby**

*   **As a** Player,
*   **I want** a waiting lobby where players can gather before the game starts,
*   **So that** we can coordinate roles and wait for the game to be full.

**Acceptance Criteria:**
1.  The lobby displays the four supply chain roles and which players have joined.
2.  Players can select their desired, available role.
3.  The game host can see all joined players and has the option to start the game with AI filling the empty slots.
4.  The game automatically starts when all four slots are filled by human players.

---

**Story 6.3: Synchronized Turn-Based Gameplay**

*   **As a** Player,
*   **I want** the multiplayer game to proceed in synchronized weekly turns,
*   **So that** all players make their decisions for the week before the game advances.

**Acceptance Criteria:**
1.  The game does not advance to the next week until all human players have submitted their orders.
2.  The UI clearly indicates which players have submitted their orders for the current week.
3.  A turn timer is implemented to prevent indefinite waiting; if a player times out, the host can have an AI take over.
4.  Player presence indicators (e.g., online/offline status) are displayed.

---

**Story 6.4: Multiplayer Game Summary**

*   **As a** Player,
*   **I want** to see a comparative summary at the end of a multiplayer game,
*   **So that** I can see how my performance compares to the other players in my supply chain.

**Acceptance Criteria:**
1.  The summary screen displays the final costs and key performance metrics for all four players side-by-side.
2.  The total supply chain cost (sum of all players) is displayed.
3.  A visualization shows the bullwhip effect across all four human-played positions.
4.  Each player receives a personalized, AI-generated analysis of their performance in the context of the team's actions.
