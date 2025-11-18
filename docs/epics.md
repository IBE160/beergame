# ibe160 - Epic Breakdown

**Author:** BIP
**Date:** 2025-11-13
**Project Level:** Level 2 (BMad Method - Greenfield SaaS)
**Target Scale:** 100+ concurrent users, 50+ game sessions

---

## Overview

This document provides the complete epic and story breakdown for ibe160, decomposing the requirements from the [PRD](./PRD.md) into implementable stories.

### Epic Summary

The platform is organized into **8 sequential epics** that build upon each other to deliver the complete AI-powered Beer Game educational platform:

1. **Foundation & Core Infrastructure** - Establish technical foundation (auth, database, deployment, security)
2. **Beer Game Simulation Engine** - Implement core supply chain mechanics and game logic
3. **Single-Player Experience** - Deliver Free and Paid Student gameplay with full UI
4. **AI Integration** - Add intelligent opponents and AI-generated assessments (competitive moat)
5. **Subscription & Payment System** - Enable revenue generation via Stripe integration
6. **Multiplayer Game Experience** - Implement collaborative Class Student gameplay
7. **Instructor Classroom Management** - Build classroom tools that save 5+ hours per class
8. **Analytics, Reporting & Organization Branding** - Complete instructor platform with insights and customization

**Sequencing Strategy:** Foundation → Core Game → Single Player → AI Intelligence → Monetization → Multiplayer → Classroom Management → Analytics

Each epic contains 5-10 stories sized for single-session completion by a 200k context development agent.

---

## Epic 1: Foundation & Core Infrastructure

**Goal:** Establish the technical foundation that enables all subsequent development, including project structure, authentication, database, deployment pipeline, and core security infrastructure.

**Business Value:** Without this foundation, no features can be built. This epic creates the scaffolding for rapid, secure development of all user-facing functionality.

### Story 1.1: Project Initialization & Repository Setup

As a developer,
I want a properly structured monorepo with Next.js frontend and FastAPI backend,
So that I have a clean foundation for rapid development with clear separation of concerns.

**Acceptance Criteria:**

**Given** I'm starting a greenfield project
**When** I initialize the repository
**Then** I have a working monorepo structure with `/frontend` and `/backend` directories

**And** Frontend uses Next.js 14+ with TypeScript, Tailwind CSS, and Shadcn UI
**And** Backend uses FastAPI with Python 3.11+, Pydantic, and UV for package management
**And** Both have linting (ESLint, Prettier, Ruff) and formatting configured
**And** Git repository has .gitignore configured for both environments
**And** README.md documents project structure and setup instructions

**Prerequisites:** None (first story)

**Technical Notes:** Use `npx create-next-app@latest` with TypeScript and Tailwind. Initialize FastAPI with `uv init`. Set up monorepo structure with clear separation. Configure VS Code workspace settings for optimal DX.

---

### Story 1.2: Next.js Frontend Application Structure

As a developer,
I want a well-organized Next.js frontend with component architecture and routing,
So that I can rapidly build user interfaces with consistency and maintainability.

**Acceptance Criteria:**

**Given** I have the project initialized
**When** I set up the frontend structure
**Then** I have organized directories: `/app` (Next.js App Router), `/components`, `/lib`, `/hooks`, `/types`

**And** Shadcn UI is installed with initial components (Button, Card, Input, Form)
**And** Tailwind CSS is configured with custom theme matching design system
**And** TypeScript is configured with strict mode enabled
**And** Basic layout component exists with navigation structure
**And** Landing page renders successfully at `/`

**Prerequisites:** Story 1.1 (project initialization)

**Technical Notes:** Use Shadcn UI for component library. Set up absolute imports with `@/` prefix. Create layout.tsx with metadata configuration. Implement responsive navigation shell.

---

### Story 1.3: FastAPI Backend Application Structure

As a developer,
I want a well-organized FastAPI backend with clear API structure and middleware,
So that I can build scalable, type-safe APIs with automatic documentation.

**Acceptance Criteria:**

**Given** I have the project initialized
**When** I set up the backend structure
**Then** I have organized directories: `/app` (FastAPI app), `/models`, `/schemas`, `/services`, `/api/routes`, `/core`

**And** FastAPI app initializes with CORS middleware configured
**And** API versioning is implemented (`/api/v1/` prefix)
**And** OpenAPI/Swagger documentation is accessible at `/docs`
**And** Health check endpoint (`/api/v1/health`) returns status
**And** Environment variable management is configured with Pydantic Settings

**Prerequisites:** Story 1.1 (project initialization)

**Technical Notes:** Use Pydantic v2 for request/response models. Configure CORS to allow frontend origin. Set up proper logging with structured output. Create base response models for consistency.

---

### Story 1.4: Database Schema Design & Supabase Setup

As a developer,
I want a comprehensive database schema and Supabase configuration,
So that I can persist all platform data with proper relationships and security.

**Acceptance Criteria:**

**Given** I need to store users, games, rounds, assessments, and classroom data
**When** I design and implement the database schema
**Then** I have 12+ core tables created: users, subscriptions, games, game_rounds, game_players, assessments, assessment_questions, assessment_responses, classes, class_students, seats, organizations

**And** All tables have proper primary keys, foreign keys, and indexes
**And** Database migration files are version-controlled (Alembic or Supabase migrations)
**And** Supabase project is created and connection string is configured
**And** Connection pooling is configured in backend
**And** Database schema diagram is documented

**Prerequisites:** Story 1.3 (backend structure)

**Technical Notes:** Design for multi-tenancy with proper data isolation. Include created_at/updated_at timestamps on all tables. Set up composite indexes for frequent queries (e.g., game_rounds by game_id and round_number). Use ENUM types for user roles and game status.

---

### Story 1.5: User Authentication System (Supabase Auth)

As a user,
I want to register and log in securely with email verification,
So that I can access the platform with a protected account.

**Acceptance Criteria:**

**Given** I'm a new user
**When** I register with email and password
**Then** I receive an email verification link within 60 seconds

**And** I cannot access protected features until email is verified
**And** Login returns a JWT token that persists for 30 days (with "remember me")
**And** Password reset flow works via email link
**And** CAPTCHA protection prevents bot registrations (95%+ success rate)
**And** Frontend has registration, login, and password reset pages
**And** Backend validates JWT tokens on protected endpoints

**Prerequisites:** Story 1.2, 1.3, 1.4 (frontend, backend, database ready)

**Technical Notes:** Use Supabase Auth client library. Store JWT in httpOnly cookies (or secure localStorage with XSS protection). Implement password complexity requirements (min 8 chars). Add rate limiting on auth endpoints (5 attempts per 15 minutes).

---

### Story 1.6: Authorization & Row Level Security (RLS)

As a developer,
I want role-based access control and Row Level Security implemented,
So that users can only access data they're authorized to see.

**Acceptance Criteria:**

**Given** I have users with different roles (Free, Paid Student, Instructor, Class Student)
**When** I implement authorization
**Then** Row Level Security (RLS) policies are enabled on all tables

**And** Users can only read/write their own data (games, assessments, profile)
**And** Instructors can read/write their classes and enrolled students' data
**And** Class Students can read game data for games they're assigned to
**And** Backend middleware validates JWT and extracts user role
**And** API endpoints enforce role-based permissions at the route level
**And** Security test suite validates RLS policies prevent unauthorized access

**Prerequisites:** Story 1.5 (authentication implemented)

**Technical Notes:** Create RLS policies using Supabase dashboard or SQL migrations. Use JWT claims to store user role. Implement backend RBAC decorator (@require_role). Test with different user roles to verify data isolation. Document permission matrix.

---

### Story 1.7: Deployment Pipeline & Production Environment

As a developer,
I want automated CI/CD deployment to production,
So that code changes deploy automatically with minimal manual intervention.

**Acceptance Criteria:**

**Given** I have working frontend and backend applications
**When** I push code to the main branch
**Then** Frontend automatically deploys to Vercel

**And** Backend (FastAPI) automatically deploys to Vercel serverless functions
**And** Environment variables are configured in Vercel (database URL, API keys, etc.)
**And** Production Supabase project is separate from development
**And** Deployment completes within 5 minutes
**And** Health check endpoint confirms successful deployment
**And** HTTPS is enforced on all production endpoints

**Prerequisites:** Story 1.3, 1.4 (backend and database setup)

**Technical Notes:** Configure Vercel project with two apps (frontend + backend). Set up Vercel environment variables for DATABASE_URL, SUPABASE_URL, SUPABASE_ANON_KEY, JWT_SECRET. Configure custom domain if available. Set up monitoring with Vercel Analytics.

---

### Story 1.8: Core API Documentation & Testing Infrastructure

As a developer,
I want comprehensive API documentation and test infrastructure,
So that I can develop with confidence and maintain quality.

**Acceptance Criteria:**

**Given** I have a working API
**When** I access `/docs` endpoint
**Then** I see complete OpenAPI/Swagger documentation for all endpoints

**And** Documentation includes request/response schemas with examples
**And** Authentication requirements are clearly documented
**And** Unit testing framework is set up (Pytest for backend, Jest for frontend)
**And** Test database is configured for integration tests
**And** CI pipeline runs tests automatically on pull requests
**And** Code coverage reporting is configured (target 80% for core logic)

**Prerequisites:** Story 1.3 (backend API structure)

**Technical Notes:** FastAPI generates OpenAPI docs automatically - enhance with detailed descriptions and examples. Use Pytest fixtures for test database setup. Configure GitHub Actions or Vercel CI for automated testing. Set up coverage.py for backend, Jest coverage for frontend.

## Epic 2: Beer Game Simulation Engine

**Goal:** Implement the core Beer Game mechanics with accurate supply chain simulation logic that produces the educational bullwhip effect.

**Business Value:** The simulation engine is the heart of the platform - without accurate Beer Game mechanics, the educational value is lost. This epic delivers the core learning experience.

### Story 2.1: Core Supply Chain Data Models

As a developer,
I want complete data models for games, positions, orders, and inventory,
So that I can accurately track all supply chain state throughout the game.

**Acceptance Criteria:**

**Given** I'm implementing Beer Game logic
**When** I create the data models
**Then** I have Pydantic models for: Game, Position (Retailer/Wholesaler/Distributor/Factory), Order, InventoryState, CostAccumulator

**And** Game model includes: configuration (weeks, costs, lead times, difficulty), current week, status, created date
**And** Position model tracks: inventory on-hand, inventory in-transit, backlog, orders received, orders placed
**And** Models include validation rules (no negative inventory, valid cost parameters)
**And** Database models (SQLAlchemy) match Pydantic schemas with proper relationships
**And** Unit tests validate model behavior and constraints

**Prerequisites:** Story 1.4 (database schema)

**Technical Notes:** Use Pydantic v2 for validation. Create separate schemas for request, response, and database models. Implement custom validators for game configuration constraints. Document all model fields with clear descriptions.

---

### Story 2.2: Four-Echelon Supply Chain Logic

As a developer,
I want the core four-echelon supply chain implemented with proper order flow,
So that beer orders flow correctly from Retailer → Wholesaler → Distributor → Factory.

**Acceptance Criteria:**

**Given** I have a game with four positions
**When** orders are placed and fulfilled
**Then** Retailer receives demand from customers (external)

**And** Retailer places orders to Wholesaler based on demand and inventory
**And** Wholesaler places orders to Distributor based on Retailer's orders
**And** Distributor places orders to Factory based on Wholesaler's orders
**And** Factory produces beer based on Distributor's orders
**And** Orders respect configurable lead times (default: 2-week shipping, 2-week production)
**And** Backlog accumulates when inventory cannot fulfill orders
**And** Unit tests verify order flow through all four echelons

**Prerequisites:** Story 2.1 (data models)

**Technical Notes:** Implement as service class (SupplyChainEngine). Use queue data structure for in-transit orders. Create helper methods for each echelon's unique behavior (Factory has production delay, others have shipping delay only). Test with known scenarios that produce bullwhip effect.

---

### Story 2.3: Turn Processing & State Updates

As a developer,
I want turn-by-turn game progression with atomic state updates,
So that each week advances correctly and all calculations are accurate.

**Acceptance Criteria:**

**Given** I have a game in progress
**When** a turn is processed
**Then** Orders are fulfilled from on-hand inventory (first-in-first-out)

**And** Unfulfilled orders add to backlog
**And** In-transit orders advance by one week (arrive after lead time)
**And** Newly placed orders enter the transit queue
**And** Inventory on-hand updates based on arrivals and fulfillments
**And** Costs accrue for holding inventory and backlog (per unit per week)
**And** All state updates occur atomically (transaction-based)
**And** Turn history is persisted to database (game_rounds table)

**Prerequisites:** Story 2.2 (supply chain logic)

**Technical Notes:** Implement turn processing as atomic database transaction. Calculate costs after state updates. Store complete turn snapshot in game_rounds for analysis and replay. Handle edge cases (negative inventory becomes backlog, zero orders).

---

### Story 2.4: Demand Pattern Generation

As a developer,
I want realistic demand patterns generated for customer orders,
So that the Retailer faces authentic supply chain variability.

**Acceptance Criteria:**

**Given** I'm starting a new game
**When** demand patterns are generated
**Then** Fixed demand pattern is available (e.g., 4 units for 4 weeks, then 8 units for remaining weeks)

**And** Demand can be pre-generated for all weeks or generated turn-by-turn
**And** Demand patterns are reproducible (seeded random for testing)
**And** Difficult games have more variability in demand
**And** Easy games have stable, predictable demand
**And** Demand values are stored in database with game configuration

**Prerequisites:** Story 2.1 (data models)

**Technical Notes:** Start with fixed MIT Beer Game demand pattern (4, 4, 4, 4, then 8 for rest). For variable demand, use configurable mean and standard deviation. Store demand pattern in game configuration. Later epics can add advanced patterns (seasonal, trend-based).

---

### Story 2.5: Inventory & Cost Calculation Engine

As a developer,
I want precise inventory tracking and cost calculations,
So that game results accurately reflect supply chain performance.

**Acceptance Criteria:**

**Given** I'm calculating costs for a turn
**When** the calculation runs
**Then** Holding cost = (on-hand inventory at end of week) × (holding cost rate per unit)

**And** Backlog cost = (backlog at end of week) × (backlog cost rate per unit)
**And** Total cost = sum of holding costs + backlog costs across all weeks
**And** Costs are calculated per position and aggregated for total game cost
**And** Cost breakdown is available (by week, by position, by cost type)
**And** Edge case handled: inventory can never go negative (becomes backlog instead)
**And** Unit tests validate cost calculations match MIT Beer Game rules

**Prerequisites:** Story 2.3 (turn processing)

**Technical Notes:** Default costs: $0.50/unit/week holding, $1.00/unit/week backlog. Store costs per turn in game_rounds table. Implement as pure functions for testability. Validate against known Beer Game outcomes.

---

### Story 2.6: Game Configuration & Initialization

As a developer,
I want flexible game configuration with validation,
So that users can customize games while maintaining valid parameters.

**Acceptance Criteria:**

**Given** I'm creating a new game
**When** I provide configuration parameters
**Then** I can configure: duration (20-52 weeks), holding cost ($0.10-$2.00), backlog cost ($0.50-$5.00), shipping lead time (1-4 weeks), production lead time (1-4 weeks), initial inventory (0-20 units), difficulty (Easy/Medium/Hard), information visibility (Full/Limited)

**And** Configuration validation prevents invalid combinations
**And** Default configuration matches MIT Beer Game (20 weeks, $0.50 holding, $1.00 backlog, 2-week shipping, 2-week production, 12 units initial inventory)
**And** Game initialization creates all four positions with starting state
**And** API endpoint accepts configuration and returns created game ID
**And** Configuration is stored with game for entire session

**Prerequisites:** Story 2.1, 2.4 (data models, demand patterns)

**Technical Notes:** Use Pydantic for configuration validation. Create GameConfigSchema with field validators. Implement factory pattern for game initialization. Store configuration as JSON in database. Provide preset configurations (Easy/Medium/Hard).

---

### Story 2.7: Game State Management & Persistence

As a developer,
I want robust game state persistence and retrieval,
So that games can be paused, resumed, and analyzed at any point.

**Acceptance Criteria:**

**Given** I have a game in progress
**When** state is updated
**Then** Complete game state is persisted after every turn (within 500ms)

**And** State includes: current week, all position inventories, all in-transit orders, all backlogs, accumulated costs
**And** Game can be retrieved and resumed from any saved state
**And** State is validated on load (data integrity checks)
**And** Historical state (all previous weeks) is accessible for analysis
**And** Database queries are optimized (indexed) for fast state retrieval
**And** Concurrent state updates are handled safely (transaction isolation)

**Prerequisites:** Story 2.3 (turn processing)

**Technical Notes:** Store state snapshots in game_rounds table. Use database transactions for atomic updates. Implement optimistic locking for concurrent updates. Create indexes on game_id and round_number. Provide API endpoints: GET /games/{id}/state, GET /games/{id}/history.

## Epic 3: Single-Player Experience (Free & Paid Students)

**Goal:** Deliver the complete single-player game experience for Free and Paid Student tiers, including game dashboard UI, visualizations, and game history.

**Business Value:** This epic creates the first complete user journey - from game start to completion - enabling revenue generation from Paid Students.

### Story 3.1: Game Dashboard UI & Layout

As a student,
I want a clear game dashboard showing my current position and game state,
So that I can make informed ordering decisions.

**Acceptance Criteria:**

**Given** I'm playing a Beer Game
**When** I view the game dashboard
**Then** I see: Current week / total weeks, my position (Retailer/Wholesaler/etc.), inventory on-hand, inventory in-transit, backlog, most recent order received, current costs

**And** Dashboard uses responsive layout (works on 768px+ screens)
**And** UI follows design system (Shadcn UI components)
**And** Dashboard updates in real-time after turn submission (<1 second)
**And** Error states are clearly communicated
**And** Loading states show during API calls

**Prerequisites:** Story 1.2, 2.7 (frontend structure, game state API)

**Technical Notes:** Use Shadcn Card components for layout. Create custom hooks for game state management (useGameState). Implement Zustand store for client-side state. Use React Query for API data fetching with automatic refresh.

---

### Story 3.2: Order Entry & Turn Submission

As a student,
I want to enter my order quantity and submit my turn,
So that I can participate in the supply chain simulation.

**Acceptance Criteria:**

**Given** I'm on my turn in the game
**When** I enter an order quantity
**Then** Input validation prevents invalid values (0-99 units, integers only)

**And** Submit button is enabled only when valid order is entered
**And** Turn submission triggers API call to POST /api/v1/games/{id}/orders
**And** Turn processes within 2 seconds
**And** UI updates immediately with new game state
**And** Success/error feedback is clear
**And** Historical orders are visible in turn history table

**Prerequisites:** Story 3.1 (dashboard UI)

**Technical Notes:** Use React Hook Form with Zod validation. Implement optimistic UI updates. Handle API errors gracefully with retry logic. Disable input during AI opponent moves. Show loading spinner during turn processing.

---

### Story 3.3: Real-Time Visualizations (Charts & Graphs)

As a student,
I want to see charts of inventory, costs, and orders over time,
So that I can understand supply chain dynamics visually.

**Acceptance Criteria:**

**Given** I'm viewing game progress
**When** I access the visualizations panel
**Then** I see: Inventory over time (line chart), Costs over time (stacked area: holding + backlog), Orders vs. Demand (dual-line chart), Bullwhip effect visualization (amplification across echelons)

**And** Charts update in real-time as turns progress
**And** Charts are interactive (hover for details, zoom, pan)
**And** Charts use consistent color scheme
**And** Charts render within 500ms after data fetch
**And** Mobile/tablet responsiveness maintained

**Prerequisites:** Story 3.1, 2.7 (dashboard, game history API)

**Technical Notes:** Use Recharts library. Create reusable chart components. Fetch turn history from API. Calculate bullwhip amplification ratio (variance of orders / variance of demand). Use Tailwind for consistent styling.

---

### Story 3.4: Role Selection & Game Initialization

As a student,
I want to select my role and start a new game,
So that I can begin playing the Beer Game.

**Acceptance Criteria:**

**Given** I'm a registered user
**When** I start a new game
**Then** I can select one role: Retailer, Wholesaler, Distributor, or Factory

**And** Free users see fixed configuration (20 weeks, default costs, Medium difficulty)
**And** Paid Students see full configuration options (weeks, costs, lead times, difficulty, visibility)
**And** Configuration form uses Shadcn UI with validation
**And** Game creation calls POST /api/v1/games with configuration
**And** Game initializes within 2 seconds
**And** I'm redirected to game dashboard after successful creation
**And** Rate limiting is enforced for Free users (3 games/day, 1 concurrent)

**Prerequisites:** Story 1.5, 2.6, 3.1 (authentication, game configuration API, dashboard)

**Technical Notes:** Create multi-step form for game setup. Store tier-based permissions in frontend state. Show upgrade prompt when Free users hit rate limits. Use React Router for navigation. Persist game ID in URL for sharing.

---

### Story 3.5: Save/Resume Functionality (Paid Students Only)

As a Paid Student,
I want to save my game and resume later,
So that I'm not forced to complete games in one session.

**Acceptance Criteria:**

**Given** I'm a Paid Student with an active game
**When** I save the game
**Then** Game state is persisted to database immediately

**And** I can safely close browser/app
**And** When I return, I see "Resume Game" option
**And** Resuming loads exact game state (week, inventory, costs, orders)
**And** I can have multiple saved games
**And** Saved games list shows: game ID, role, current week, last played date
**And** Free users do not see save/resume options (tier-gated feature)

**Prerequisites:** Story 3.4, 2.7 (game initialization, state management)

**Technical Notes:** Add "Save & Exit" button to dashboard. Update game status to "paused" in database. Create /games endpoint listing user's games. Filter by status (in_progress, paused, completed). Implement tier check on frontend and backend.

---

### Story 3.6: Post-Game Summary & Analysis

As a student,
I want to see comprehensive results after completing a game,
So that I can understand my performance and learn from the experience.

**Acceptance Criteria:**

**Given** I've completed a 20-week game
**When** the game ends
**Then** I see post-game summary: Total cost, final inventory, cost breakdown (holding vs. backlog by position), performance comparison (optimal vs. my play)

**And** Visualizations show complete game: Bullwhip effect diagram, inventory timeline, order amplification
**And** Free users see basic summary only
**And** Paid Students see AI-generated insights (decision pattern analysis)
**And** Summary is accessible from game history
**And** Summary loads within 3 seconds

**Prerequisites:** Story 3.3, 2.7 (visualizations, complete game data)

**Technical Notes:** Calculate optimal play baseline for comparison. Create summary page layout. Store summary data in database for fast retrieval. Add "Play Again" button to start new game. Link to assessment (Epic 4) for Paid Students.

---

### Story 3.7: Personal Game History (Paid Students Only)

As a Paid Student,
I want to access my complete game history,
So that I can track improvement and review past games.

**Acceptance Criteria:**

**Given** I'm a Paid Student who has completed multiple games
**When** I access my game history
**Then** I see list of all games: Date, role, total cost, score, difficulty, completion status

**And** I can filter by: date range, role, difficulty, score
**And** I can sort by: date, score, duration
**And** I can replay past games (view turn-by-turn)
**And** I can export game data as CSV
**And** I can delete games from history
**And** Pagination handles 100+ games efficiently

**Prerequisites:** Story 3.6 (post-game summary)

**Technical Notes:** Create /profile/games route. Use Shadcn Table component with sorting/filtering. Implement pagination (20 games per page). Add replay viewer showing turn-by-turn state. Use react-csv for export. Confirm before deletion.

---

## Epic 4: AI Integration - Opponents & Assessments

**Goal:** Implement AI-powered opponents and assessment generation - the platform's core competitive differentiator.

**Business Value:** This is THE magic. AI opponents create realistic bullwhip effects, and personalized assessments drive learning outcomes no competitor can match.

### Story 4.1: Pydantic AI Setup & Provider Configuration

As a developer,
I want Pydantic AI configured with multiple LLM providers,
So that I can switch between models and manage costs effectively.

**Acceptance Criteria:**

**Given** I'm integrating AI capabilities
**When** I configure Pydantic AI
**Then** Gemini Flash and Gemini Pro are configured as providers

**And** Provider selection is environment-variable controlled
**And** API keys are securely stored (environment variables, not hardcoded)
**And** Connection testing validates provider availability
**And** Fallback provider is configured (if Gemini unavailable, use rule-based AI)
**And** Usage tracking logs all API calls for cost monitoring
**And** Rate limiting prevents excessive API calls

**Prerequisites:** Story 1.3, 1.8 (backend structure, API setup)

**Technical Notes:** Install pydantic-ai library. Create AIProvider service class. Implement provider factory pattern. Store API keys in .env file. Create health check endpoint testing AI connectivity. Log usage to database for cost analysis.

---

### Story 4.2: AI Opponent - Decision Generation

As a student,
I want AI opponents that make realistic supply chain decisions,
So that I experience authentic bullwhip effects during gameplay.

**Acceptance Criteria:**

**Given** I'm playing against AI opponents (3 other positions)
**When** it's an AI's turn
**Then** AI generates order quantity within 3 seconds

**And** AI decisions consider: current inventory, recent demand, backlog, position-specific constraints
**And** AI demonstrates human-like behavior: overreaction to stockouts, panic ordering, gradual adjustment, cognitive biases
**And** AI produces bullwhip effect 90%+ of games (orders amplify upstream)
**And** Free users get Gemini Flash (cost-effective)
**And** Paid Students get Gemini Pro (higher quality)
**And** AI decision consistency is 95%+ (same inputs → similar outputs)

**Prerequisites:** Story 4.1, 2.3 (Pydantic AI setup, turn processing)

**Technical Notes:** Create detailed prompts for each position's decision-making. Use structured output (Pydantic models) for order quantities. Implement prompt engineering techniques (few-shot examples, chain-of-thought). Cache common scenarios. Fallback to rule-based AI if LLM fails. Test against MIT Beer Game benchmarks.

---

### Story 4.3: AI Assessment Generation

As a Paid Student,
I want AI-generated assessments based on my gameplay,
So that I receive personalized learning feedback.

**Acceptance Criteria:**

**Given** I've completed a game
**When** assessment generation runs
**Then** AI generates 8-12 questions within 10 seconds

**And** Question types: 40% multiple choice, 30% short text, 20% long text, 10% numeric
**And** Questions reference specific game turns and decisions (e.g., "In round 7, you ordered 15 units when backlog was 8...")
**And** Questions cover supply chain concepts: bullwhip effect, inventory management, lead time impacts, cost trade-offs
**And** Cognitive levels: 30% recall, 40% application, 30% analysis
**And** Questions are pedagogically sound (instructor review = 4.0+ out of 5.0 relevance)
**And** Question bank is stored in database (assessment_questions table)

**Prerequisites:** Story 4.1, 3.6 (AI setup, post-game data)

**Technical Notes:** Create assessment prompt with game history context. Use Pydantic models for structured question output (Question, Options, Answer, Explanation). Implement question type generators. Store questions with metadata (difficulty, concept tested). Allow instructor review/override in Epic 7.

---

### Story 4.4: AI Feedback & Automated Scoring

As a Paid Student,
I want instant feedback on my assessment answers,
So that I understand supply chain concepts immediately.

**Acceptance Criteria:**

**Given** I've submitted assessment answers
**When** AI grades my responses
**Then** Grading completes within 5 seconds

**And** Multiple choice: Rule-based scoring (correct/incorrect)
**And** Numeric: Tolerance-based scoring (within 5% = correct)
**And** Short/long text: AI evaluates against rubric and provides score (0-100%)
**And** Weighted scoring: MC (1 pt), short text (2 pts), long text (3 pts), numeric (2 pts)
**And** Feedback explains concepts and connects to specific game decisions
**And** Pass/fail determined by configurable threshold (default 70%)
**And** Grading accuracy: 85%+ matches instructor review

**Prerequisites:** Story 4.3 (assessment generation)

**Technical Notes:** Create grading prompts with rubrics. Use Pydantic structured output for scores and feedback. Store responses and scores in assessment_responses table. Implement retry logic for AI failures. Provide detailed feedback for incorrect answers.

---

### Story 4.5: AI Cost Management & Caching

As the platform,
I want AI API costs controlled and optimized,
So that the business remains profitable.

**Acceptance Criteria:**

**Given** I'm using AI for opponents and assessments
**When** I monitor costs
**Then** AI costs are <20% of revenue for Free tier, <15% for Paid tiers

**And** Common AI responses are cached (30%+ cache hit rate)
**And** Cache stores: opponent decisions for similar scenarios, assessment questions for similar games
**And** Cache expiration is configured (7 days for opponents, 30 days for assessments)
**And** Usage monitoring dashboard tracks: API calls per user, cost per game, cost per assessment
**And** Alerts trigger when costs exceed thresholds
**And** Rate limiting prevents abuse (max 10 games/day for Free, unlimited for Paid)

**Prerequisites:** Story 4.1, 4.2, 4.3 (AI setup, opponents, assessments)

**Technical Notes:** Implement Redis or database caching layer. Hash game scenarios for cache keys. Track usage in database (ai_usage table). Create monitoring dashboard in backend. Set up cost alerts via email. Implement tier-based rate limiting.

---

## Epic 5: Subscription & Payment System

**Goal:** Enable revenue generation through Stripe integration for subscriptions and seat purchases.

**Business Value:** Monetization infrastructure is critical - without payments, there's no business model.

### Story 5.1: Stripe Integration & Webhook Setup

As a developer,
I want Stripe integrated with webhook handling,
So that subscription and payment events are processed reliably.

**Acceptance Criteria:**

**Given** I'm setting up payment infrastructure
**When** I configure Stripe
**Then** Stripe API keys are configured (test and production)

**And** Webhook endpoints are created: /api/v1/webhooks/stripe
**And** Webhook signature verification is implemented (prevents fraud)
**And** Webhook events are handled: customer.subscription.created, customer.subscription.updated, customer.subscription.deleted, invoice.payment_succeeded, invoice.payment_failed, charge.refunded
**And** Failed webhooks are retried (3 attempts with exponential backoff)
**And** Webhook processing completes within 5 seconds
**And** All webhook events are logged for debugging

**Prerequisites:** Story 1.3, 1.4 (backend API, database)

**Technical Notes:** Install stripe library. Create StripeService class. Implement webhook handler with signature verification. Store subscription data in subscriptions table. Use idempotency keys. Log events to stripe_events table. Test with Stripe CLI.

---

### Story 5.2: Subscription Tier Management

As a user,
I want to subscribe to Paid Student or Instructor tier,
So that I can access premium features.

**Acceptance Criteria:**

**Given** I'm a Free user
**When** I upgrade to Paid Student ($5/month) or Instructor ($29.99/month)
**Then** Stripe Checkout session is created with correct pricing

**And** Payment succeeds and subscription activates immediately
**And** User role updates in database (free → paid_student or instructor)
**And** User gains access to tier-specific features instantly
**And** Subscription auto-renews monthly
**And** Proration is handled for mid-cycle upgrades/downgrades
**And** Invoices are emailed automatically

**Prerequisites:** Story 5.1 (Stripe integration)

**Technical Notes:** Create Stripe Products and Prices in dashboard. Implement /api/v1/subscriptions/create endpoint. Use Stripe Checkout for payment UI. Handle success/cancel redirect URLs. Update user.role in database after webhook confirmation. Store Stripe customer_id and subscription_id.

---

### Story 5.3: Seat Purchase System (Instructor Only)

As an Instructor,
I want to purchase seats for Class Students,
So that I can enroll students in my classes.

**Acceptance Criteria:**

**Given** I'm a Paid Instructor
**When** I purchase seats
**Then** I select quantity and see bulk pricing applied: 1-25 seats ($5 each), 26-100 ($4.50 each), 101-250 ($4 each), 251+ ($3.50 each)

**And** One-time Stripe Checkout session is created
**And** Payment succeeds and seats are added to my account immediately
**And** Seat inventory is tracked: purchased, assigned, consumed
**And** Seats are non-reusable (permanent data retention for longitudinal analytics)
**And** Seat balance is visible on instructor dashboard
**And** Purchase history is accessible

**Prerequisites:** Story 5.2 (subscription management)

**Technical Notes:** Create Stripe Price for seats with dynamic quantity pricing. Implement /api/v1/seats/purchase endpoint. Store seats in instructor_seats table (instructor_id, quantity, purchased_date). Decrement available seats on assignment. Prevent seat reuse with consumed flag.

---

### Story 5.4: Subscription Management & Cancellation

As a user,
I want to manage my subscription (upgrade, downgrade, cancel),
So that I have control over my account.

**Acceptance Criteria:**

**Given** I have an active subscription
**When** I manage my subscription
**Then** I can upgrade (Student → Instructor), downgrade (Instructor → Student), or cancel

**And** Upgrades take effect immediately with proration
**And** Downgrades take effect at period end
**And** Cancellation preserves access until period end (no refund)
**And** Grace period for failed payments (3 days before downgrade to Free)
**And** Cancellation flow includes feedback collection
**And** Users can reactivate cancelled subscriptions

**Prerequisites:** Story 5.2 (subscription tier management)

**Technical Notes:** Use Stripe Customer Portal for subscription management UI. Implement /api/v1/subscriptions/update and /api/v1/subscriptions/cancel endpoints. Handle subscription status changes via webhooks. Store cancellation feedback in database. Send confirmation emails.

---

### Story 5.5: Payment History & Invoicing

As a user,
I want to access my payment history and invoices,
So that I have records for accounting/budgeting.

**Acceptance Criteria:**

**Given** I have made payments
**When** I access payment history
**Then** I see list of all transactions: date, amount, description, status, invoice link

**And** I can download PDF invoices from Stripe
**And** Payment history includes: subscriptions, seat purchases, refunds
**And** Failed payment attempts are visible with retry status
**And** Invoices are emailed automatically after each charge
**And** Payment history is exportable as CSV

**Prerequisites:** Story 5.2, 5.3 (subscriptions, seat purchases)

**Technical Notes:** Create /profile/payments route. Fetch data from Stripe API and local database. Use Stripe hosted invoice URLs. Implement pagination. Add email delivery via SendGrid. Ensure GDPR compliance (user can export all payment data).

---

## Epic 6: Multiplayer Game Experience (Class Students)

**Goal:** Implement collaborative multiplayer gameplay for Class Students with turn synchronization and AFK management.

**Business Value:** Multiplayer enables classroom learning and unlocks the Class Student revenue stream ($5/seat).

### Story 6.1: Multiplayer Session Setup & Player Assignment

As an Instructor,
I want to create multiplayer game sessions with assigned students,
So that students can play collaboratively.

**Acceptance Criteria:**

**Given** I'm setting up a class game
**When** I assign students to a game
**Then** 1-4 students are assigned to one game

**And** Each student is assigned one position (Retailer, Wholesaler, Distributor, Factory)
**And** Unassigned positions are filled by AI opponents
**And** All students in the game share the same configuration (duration, costs, difficulty)
**And** Game status is "waiting" until all students join
**And** Students receive email/notification with game link

**Prerequisites:** Story 2.6, 5.3 (game configuration, seat system)

**Technical Notes:** Create game_players table linking users to games with positions. Implement /api/v1/games/{id}/assign endpoint. Send invitations via SendGrid. Use game status state machine (waiting → active → completed). Auto-fill with AI if fewer than 4 players.

---

### Story 6.2: Turn Synchronization & Real-Time Updates

As a Class Student,
I want to see real-time updates when other players submit orders,
So that I know when it's my turn and when the game progresses.

**Acceptance Criteria:**

**Given** I'm in a multiplayer game
**When** a player submits their order
**Then** All players see real-time status update within 2 seconds

**And** Turn advances only when all players submit orders (or AI takes over)
**And** Player presence indicators show online/offline status
**And** Turn timer shows how long current turn has been active
**And** Game proceeds automatically after all orders submitted
**And** Network interruptions are handled gracefully (reconnect preserves state)

**Prerequisites:** Story 6.1, 2.7 (player assignment, game state management)

**Technical Notes:** Use Supabase Realtime subscriptions for game state updates. Subscribe to game_rounds table. Emit events on order submission. Implement presence tracking via Supabase Presence API. Handle reconnection with state synchronization.

---

### Story 6.3: AFK Player Detection & AI Takeover

As a Class Student,
I want the game to continue even if a player goes AFK,
So that my learning experience isn't blocked by inactive players.

**Acceptance Criteria:**

**Given** A player hasn't submitted an order
**When** 2 minutes have passed (configurable)
**Then** Warning notification appears at 30 seconds remaining

**And** "Nudge" button allows other players to send reminder
**And** After 2 minutes, AI automatically takes over and submits order
**And** AI takeover is temporary (player can resume next turn)
**And** Instructor can manually intervene (classroom mode)
**And** AFK events are logged for instructor visibility

**Prerequisites:** Story 6.2, 4.2 (turn synchronization, AI opponents)

**Technical Notes:** Implement turn timer on backend with 2-minute timeout. Use WebSocket/Realtime to broadcast warnings. Create AI takeover service for emergency orders. Log AFK events to game_audit table. Provide instructor override via dashboard.

---

### Story 6.4: In-Game Chat (Optional, If Enabled)

As a Class Student,
I want to chat with other players in my game,
So that I can coordinate and discuss strategy.

**Acceptance Criteria:**

**Given** Chat is enabled for my game (instructor setting)
**When** I send a message
**Then** All players in the game see the message within 2 seconds

**And** Basic profanity filtering prevents offensive language
**And** Chat history is persisted with game data
**And** Instructor can view chat history
**And** Instructor can disable chat per game
**And** Chat UI is collapsible (doesn't obstruct game view)

**Prerequisites:** Story 6.2 (real-time updates)

**Technical Notes:** Use Supabase Realtime for chat messages. Store in game_chat table. Implement simple profanity filter (word blacklist). Create ChatPanel component with auto-scroll. Make chat optional via game configuration. Ensure COPPA compliance (no PII collection).

---

### Story 6.5: Multiplayer Post-Game & Individual Assessment

As a Class Student,
I want personalized assessment based on my multiplayer performance,
So that I'm fairly evaluated on my individual contribution.

**Acceptance Criteria:**

**Given** My multiplayer game has completed
**When** I view my results
**Then** I see my individual performance: total cost, inventory, decisions

**And** I see team performance: total team cost, bullwhip analysis
**And** AI assessment is tailored to my role and specific decisions
**And** Grading accounts for position differences (Factory vs. Retailer have different challenges)
**And** Pass/fail status is based on instructor threshold (default 70%)
**And** I can view other players' performance (if instructor allows)

**Prerequisites:** Story 6.1, 4.3 (multiplayer setup, AI assessment)

**Technical Notes:** Generate role-specific assessments using position context in AI prompt. Calculate individual and team metrics. Store results in assessment_responses table linked to user and game. Implement privacy settings (instructor controls visibility).

---

## Epic 7: Instructor Classroom Management

**Goal:** Build comprehensive classroom management tools that save instructors 5+ hours per class.

**Business Value:** This is the instructor automation magic - the platform's second value pillar.

### Story 7.1: Class Creation & Management

As an Instructor,
I want to create and manage multiple classes,
So that I can organize different courses or sections.

**Acceptance Criteria:**

**Given** I'm a Paid Instructor
**When** I create a class
**Then** I provide: class name, description, semester/term, start/end dates

**And** Each class has unique identifier (class code)
**And** I can create unlimited classes
**And** I can archive completed classes (hide from active view)
**And** I can delete classes (with confirmation)
**And** Class list shows: name, student count, active games, completion rate
**And** I can view class roster and game assignments

**Prerequisites:** Story 1.6, 5.2 (authorization, instructor subscription)

**Technical Notes:** Create classes table. Implement /api/v1/classes CRUD endpoints. Generate unique class codes (8-character alphanumeric). Implement soft delete for archival. Create ClassDashboard component. Use Shadcn Table for class list.

---

### Story 7.2: Bulk Student Enrollment (CSV Import)

As an Instructor,
I want to bulk enroll students via CSV upload,
So that I can quickly add 30+ students to my class.

**Acceptance Criteria:**

**Given** I have a class created
**When** I upload a CSV file (columns: name, email)
**Then** CSV is validated: email format, duplicate detection, required fields

**And** Validation errors are clearly reported (row number, error description)
**And** I can fix errors and re-upload
**And** Valid students are bulk inserted to class_students table
**And** Email invitations are sent to all enrolled students
**And** Invitation emails include: class name, game link, registration instructions
**And** Bulk enrollment completes within 30 seconds for 100 students

**Prerequisites:** Story 7.1, 5.3 (class creation, seat system)

**Technical Notes:** Use csv-parser library. Implement multi-step wizard: upload → validate → preview → confirm. Show validation results in table. Decrement instructor's available seats. Send emails asynchronously (queue). Create invitation template in SendGrid.

---

### Story 7.3: Automated Game Allocation

As an Instructor,
I want students automatically allocated to multiplayer games,
So that I don't have to manually assign players.

**Acceptance Criteria:**

**Given** I have enrolled 30+ students
**When** I run auto-allocation
**Then** Students are distributed into games (1-4 per game)

**And** Allocation algorithm balances game sizes (prefer 4-player games)
**And** All games use common configuration (duration, costs, difficulty) for fair comparison
**And** Allocation preview shows game groups before confirmation
**And** I can manually override allocations (drag-and-drop interface)
**And** Allocation completes within 5 seconds for 100 students
**And** Students are notified of their game assignment

**Prerequisites:** Story 7.2, 6.1 (bulk enrollment, multiplayer setup)

**Technical Notes:** Implement allocation algorithm (greedy bin packing). Create allocation preview UI with game groups. Use react-beautiful-dnd for manual adjustments. Store allocations in game_players table. Trigger email notifications after confirmation.

---

### Story 7.4: Real-Time Monitoring Dashboard

As an Instructor,
I want to monitor all active games in real-time,
So that I can track class progress and identify issues.

**Acceptance Criteria:**

**Given** I have active games in my class
**When** I view the monitoring dashboard
**Then** I see all games with: game ID, player names, current week, total weeks, status (not started / in progress / completed)

**And** Dashboard updates every 5 seconds (configurable refresh rate)
**And** I can drill down to view individual game details (turn-by-turn history)
**And** Dashboard displays 50+ games simultaneously without performance degradation
**And** I can filter by status, student name, game ID
**And** Color coding indicates: on-track (green), at-risk (yellow), stalled (red)
**And** I can pause/resume individual games

**Prerequisites:** Story 7.3, 6.2 (game allocation, multiplayer real-time)

**Technical Notes:** Use Supabase Realtime to subscribe to game updates. Implement pagination/virtualization for large game lists. Create GameMonitoringCard component. Use React Query with refetchInterval. Add filters with Shadcn Select/Input components.

---

### Story 7.5: Class-Wide Controls & Communication

As an Instructor,
I want class-wide controls and communication tools,
So that I can efficiently manage all students simultaneously.

**Acceptance Criteria:**

**Given** I'm managing an active class
**When** I use class-wide controls
**Then** I can: Pause All Games, Resume All Games, Reset All Games (confirmation required), Send Message to All Students

**And** Class-wide actions complete within 10 seconds for 50+ games
**And** Broadcast messages are sent via email and in-app notification
**And** I can send direct messages to individual students
**And** Message templates exist for common scenarios (game start reminder, deadline reminder, congratulations)
**And** Message history is accessible

**Prerequisites:** Story 7.4 (monitoring dashboard)

**Technical Notes:** Implement bulk operations with batch processing. Use transaction for atomicity. Create MessageComposer component with template selection. Store messages in class_messages table. Send emails via SendGrid with BCC for broadcasts. Add notification bell icon in student UI.

---

### Story 7.6: Assessment Management & Grade Override

As an Instructor,
I want to review AI-generated assessments and override grades,
So that I maintain control over student evaluation.

**Acceptance Criteria:**

**Given** Students have completed assessments
**When** I review assessments
**Then** I see list of all students with: name, game ID, score, pass/fail status, submission date

**And** I can view individual student's assessment questions and answers
**And** I can override AI-generated scores
**And** I can change pass/fail status manually
**And** I can configure passing threshold (default 70%)
**And** I can allow resubmissions (configurable limit, default 2 attempts)
**And** Changes are logged with audit trail (timestamp, instructor action)

**Prerequisites:** Story 4.4 (AI scoring)

**Technical Notes:** Create AssessmentReview UI with table and detail view. Implement /api/v1/assessments/{id}/override endpoint. Store overrides in assessment_overrides table. Update assessment_responses with instructor_score. Log changes to audit_log table. Send notification to student on grade change.

---

## Epic 8: Analytics, Reporting & Organization Branding

**Goal:** Complete the instructor platform with analytics, reporting, and white-label customization.

**Business Value:** These features finalize the instructor value proposition with insights and institutional credibility.

### Story 8.1: Class Analytics Dashboard

As an Instructor,
I want comprehensive class analytics,
So that I can measure learning outcomes and identify trends.

**Acceptance Criteria:**

**Given** My class has completed games
**When** I view analytics dashboard
**Then** I see: Average total cost, completion rate, pass rate, average assessment score

**And** Distribution charts: Cost distribution (histogram), score distribution, time-to-completion
**And** Bullwhip effect analysis: Average amplification ratio, positions most affected
**And** Trend over time: Weekly game completions, score improvements
**And** Top performers and struggling students identified
**And** Analytics update daily (not real-time for performance)

**Prerequisites:** Story 7.6, 6.5 (assessment management, multiplayer results)

**Technical Notes:** Create analytics aggregation queries. Use database materialized views for performance. Implement AnalyticsDashboard component with Recharts. Cache calculations (refresh daily). Create helper functions for statistical calculations (mean, std dev, percentiles).

---

### Story 8.2: Longitudinal Tracking & Cohort Comparison

As an Instructor,
I want to compare performance across semesters,
So that I can track improvements and benchmark cohorts.

**Acceptance Criteria:**

**Given** I've taught multiple semesters
**When** I access longitudinal analytics
**Then** I can compare cohorts: Fall 2024 vs. Spring 2025

**And** Metrics compared: Average cost, pass rate, bullwhip amplification, improvement rate
**And** Trend lines show performance over time (semester by semester)
**And** I can filter by: game difficulty, class size, date range
**And** Comparisons account for configuration differences (e.g., Easy vs. Hard games)
**And** Statistical significance indicators show meaningful differences

**Prerequisites:** Story 8.1 (class analytics)

**Technical Notes:** Store semester/cohort metadata with classes. Implement cohort comparison queries. Create LongitudinalView component with multi-line charts. Normalize scores for fair comparison. Use basic statistical tests (t-test) for significance.

---

### Story 8.3: Exportable Reports (PDF & CSV)

As an Instructor,
I want to export reports,
So that I can share results with stakeholders or integrate with LMS.

**Acceptance Criteria:**

**Given** I have class data to export
**When** I generate a report
**Then** I can export: Class summary report (PDF), individual student reports (PDF), raw game data (CSV), assessment results (CSV)

**And** PDF reports are professionally formatted with branding
**And** CSV exports include all relevant fields (game data, costs, decisions, scores)
**And** Reports generate within 10 seconds for 50 students
**And** Reports are downloadable immediately
**And** I can schedule recurring exports (weekly summary emails)

**Prerequisites:** Story 8.1 (analytics data)

**Technical Notes:** Use libraries: puppeteer for PDF generation, csv-writer for CSV. Create report templates. Implement /api/v1/reports/generate endpoint with format parameter. Store generated reports in cloud storage (Supabase Storage). Email links for large exports.

---

### Story 8.4: Organization Branding & White-Label

As an Instructor,
I want to customize the platform with my organization's branding,
So that it looks professional and institutional.

**Acceptance Criteria:**

**Given** I'm a Paid Instructor
**When** I configure branding
**Then** I can upload organization logo (max 2MB, PNG/JPG/SVG)

**And** I can configure custom theme colors: primary, secondary, accent
**And** Branding applies to: Instructor dashboard, student game interface, emails, PDF reports
**And** I can preview branding before applying
**And** I can revert to default branding
**And** Logo uploads within 5 seconds
**And** Theme colors update immediately across all pages

**Prerequisites:** Story 1.2, 7.1 (frontend structure, class management)

**Technical Notes:** Store branding config in organizations table. Upload logos to Supabase Storage. Implement CSS custom properties for theming. Create BrandingSettings component with live preview. Apply branding via theme context. Update email templates with organization logo.

---

### Story 8.5: Student Performance Tracking (Student View)

As a student,
I want to track my personal performance over time,
So that I can see my improvement and learning progress.

**Acceptance Criteria:**

**Given** I'm a student who has completed multiple games
**When** I view my profile
**Then** I see: Total games completed, average cost, best game, improvement rate, completion streak

**And** Performance trends show cost improvements over time
**And** I can compare my performance to class average (if instructor enables)
**And** I see achievement indicators (first game completed, 10 games played, etc.)
**And** Profile loads within 2 seconds
**And** I can export my game history

**Prerequisites:** Story 3.7, 6.5 (game history, multiplayer results)

**Technical Notes:** Create StudentProfile route. Aggregate user's game data. Calculate improvement metrics (linear regression). Create comparison chart (user vs. class average). Implement privacy controls (instructor toggles visibility).

---

### Story 8.6: Data Retention & Export (GDPR Compliance)

As a user,
I want to export all my data and delete my account,
So that I have control over my personal information.

**Acceptance Criteria:**

**Given** I'm a registered user
**When** I request data export
**Then** I receive complete data package within 30 days (GDPR compliant)

**And** Export includes: Profile data, all game history, all assessments, all payments
**And** Export format is JSON (machine-readable)
**And** I can request account deletion
**And** Deletion has 7-day grace period before becoming permanent
**And** PII is removed after deletion (gameplay data anonymized for research)
**And** Confirmation emails are sent for both export and deletion

**Prerequisites:** Story 1.5, 5.5 (authentication, payment history)

**Technical Notes:** Implement /api/v1/user/export and /api/v1/user/delete endpoints. Aggregate all user data from all tables. Use JSON export format. Implement anonymization (replace user_id with anonymous ID, remove email/name). Send confirmation emails. Log deletion requests to compliance_log table.

---

_For implementation: Use the `create-story` workflow to generate individual story implementation plans from this epic breakdown._
