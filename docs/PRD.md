# ibe160 - Product Requirements Document

**Author:** BIP
**Date:** 2025-11-13
**Version:** 1.0

---

## Executive Summary

The Beer Game Interactive Platform revolutionizes supply chain education by bringing a 60-year-old MIT simulation into the AI era. This is not just another online Beer Game - it's the first AI-powered educational platform that combines intelligent opponents, automated assessment generation, and comprehensive classroom management in a modern, accessible package.

The platform serves a dual market: individual learners seeking self-directed supply chain education, and educational institutions needing efficient classroom management tools. Through a carefully designed four-tier access model (Free Demo, Paid Students at $5/month, Paid Instructors at $29.99/month, and Class Students via $5 one-time seat purchase), the platform delivers accessibility while maintaining sustainability.

Built on modern cloud-native architecture (Next.js, FastAPI, Supabase, Pydantic AI with Gemini 2.5), the platform is designed for rapid 5-week development using AI-assisted methodologies while ensuring production-grade quality and scalability.

### What Makes This Special

**The AI-Powered Learning Revolution**

This platform is the FIRST to integrate AI throughout the entire learning experience:
- **Intelligent opponents** that demonstrate realistic supply chain decision-making using Gemini 2.5 Pro
- **Context-aware assessments** automatically generated based on each student's unique gameplay patterns
- **Personalized feedback** that connects supply chain concepts directly to specific decisions made during the game
- **Real-time insights** that help students understand the bullwhip effect as it unfolds

**The "Aha!" Moment**

The magic happens when a student sees their ordering decision ripple through the supply chain, watches the AI-powered visualization show the amplification effect, and then receives an assessment question like: "In round 7, you ordered 15 units when your backlog was only 8. How did this decision contribute to the bullwhip effect you observed in rounds 10-12?"

That's when abstract theory becomes concrete understanding.

For instructors, the magic is different but equally powerful: watching 30+ students simultaneously playing multiplayer games on a real-time dashboard, with AI automatically generating personalized assessments for each one, saving 5+ hours of grading work while providing better learning outcomes than manual assessment ever could.

---

## Project Classification

**Technical Type:** SaaS B2B Web Application
**Domain:** Educational Technology (EdTech)
**Complexity:** Medium

**Project Type Analysis:**

Based on the detection signals from the Product Brief, this platform exhibits characteristics of multiple project types:

1. **Primary: SaaS B2B** - Multi-tenant platform with subscription tiers, classroom management, organization branding, role-based access control, and comprehensive analytics
2. **Secondary: Web Application** - Browser-based, real-time multiplayer, responsive design, modern SPA architecture
3. **Tertiary: EdTech** - Student privacy considerations, assessment generation, learning analytics, instructor tools

**Domain Context:**

EdTech is a medium-complexity domain requiring attention to:
- **Privacy Compliance**: While full COPPA/FERPA compliance is university/institutional responsibility, the platform must support secure data handling
- **Accessibility**: WCAG 2.1 guidelines for inclusive learning (basic AA compliance in MVP, full in post-MVP)
- **Assessment Validity**: AI-generated assessments must be pedagogically sound and relevant to learning objectives
- **Content Guidelines**: Age-appropriate content, appropriate language in AI-generated materials

The platform benefits from being in higher education/professional training (not K-12), which reduces regulatory burden while maintaining educational effectiveness standards.

### Product Magic Essence

**Dual Value Proposition:**

1. **AI Intelligence That Feels Human**: The platform's AI opponents don't just play optimally - they demonstrate realistic supply chain behavior including overreaction to stockouts, panic ordering, and gradual adjustment. Students learn by seeing authentic supply chain psychology in action, making the bullwhip effect tangible and memorable.

2. **Instructor Liberation**: Automating 5+ hours of administrative work per class isn't just time savings - it's transforming instructors from game administrators into learning facilitators. The platform handles enrollment, allocation, monitoring, and assessment generation, allowing instructors to focus on teaching supply chain concepts instead of managing logistics.

These two pillars work synergistically: authentic AI behavior creates rich learning experiences, while automation scales those experiences to entire classrooms without overwhelming instructors.

---

## Success Criteria

### MVP Success (What "Done" Looks Like)

**For Students:**
- Complete a 20-week Beer Game and immediately understand why the bullwhip effect happened in their specific game
- Receive AI-generated assessment questions that feel personal and relevant to their decisions
- Say "I finally get it" when connecting ordering behavior to downstream amplification

**For Instructors:**
- Enroll 30 students, allocate them to games, and start monitoring in under 10 minutes
- Spend 80% less time on game administration compared to traditional methods
- Trust that AI-generated assessments accurately evaluate student understanding
- See clear patterns in class performance that inform teaching moments

**For the Platform:**
- First AI-powered Beer Game simulation in the market (competitive moat)
- 60%+ instructor trial-to-paid conversion (proving value proposition)
- 4.0+ out of 5.0 rating for AI assessment relevance
- Break-even within 3-4 months (MRR ~$500)

### Business Metrics

**Revenue Growth (First 3 Months):**
- 10+ paying instructor subscribers ($29.99/month) = $299.90 MRR
- 50+ Paid Student subscribers ($5/month) = $250 MRR
- 300+ seat purchases averaging $4.50 = $1,350 one-time revenue
- **Total: $550 MRR + $1,350 seats = Break-even achieved**

**User Engagement:**
- Free → Paid Student conversion: 3-5%
- Paid Student → Instructor conversion: 2-3%
- Monthly churn: <5% for both tiers
- Average free user completes 2+ demo games before conversion/churn

**Educational Impact:**
- 80%+ of students report improved understanding of supply chain concepts
- 80%+ completion rate for assigned class games
- Students can identify and explain bullwhip effect after one game completion
- AI assessment pass rate: 60-75% (indicating appropriate difficulty)

**Technical Performance:**
- Application load time: <3 seconds on standard broadband
- Game state updates: <500ms processing time
- API response time: <200ms for 95th percentile
- System uptime: 99%+ during operating hours
- Support 100+ concurrent game sessions without degradation

**Financial Health:**
- Customer Acquisition Cost (CAC): <$15 (students), <$100 (instructors)
- Lifetime Value to CAC ratio: >3:1 for both tiers
- AI API costs: <20% of revenue (free tier), <15% (paid tiers)
- Gross margin: >60% after infrastructure and AI costs

---

## Product Scope

### MVP - Minimum Viable Product (5 Weeks)

**Core Value Delivery: Complete Four-Tier User Experience**

The MVP delivers the full value proposition for all user types, proving both the AI intelligence and instructor automation pillars.

**Tier 0 - Free Registered Users:**
- Fixed 20-week single-player Beer Game with predetermined parameters
- Role selection (Retailer, Wholesaler, Distributor, Factory)
- AI opponents using cost-effective models (Gemini Flash)
- Basic performance summary (total cost, final inventory)
- Rate limiting (3 games/day, 1 concurrent game)
- CAPTCHA protection on registration

**Tier 1 - Paid Students ($5/month):**
- All Free Tier features PLUS:
- Full game configuration (20-52 weeks, cost parameters, lead times, difficulty, visibility)
- High-ability AI opponents (Gemini Pro)
- Unlimited gameplay with save/resume functionality
- AI-generated assessments (8-12 questions: multiple choice, short text, long text, numeric)
- Instant AI-powered feedback with weighted scoring
- Comprehensive post-game analysis with AI insights
- Personal game history and performance tracking
- Enhanced visualizations (bullwhip effect analysis, decision pattern insights)

**Tier 2 - Paid Instructors ($29.99/month):**
- All Paid Student features PLUS:
- Unlimited class creation and management
- Seat purchase system with bulk pricing (1-25: $5, 26-100: $4.50, 101-250: $4, 251+: $3.50)
- Bulk student enrollment (CSV import or manual entry)
- Automated game allocation (1-4 students per game) with manual override
- Common game configuration for fair comparison
- Real-time monitoring dashboard showing all active games
- Class-wide controls (pause all, resume all, reset all)
- Individual game actions (view progress, remove student)
- AI-generated assessment system with configurable passing threshold
- Student resubmission capability with limits
- Instructor review and grade override
- Communication system (broadcast to all, direct messages)
- Analytics dashboard (class metrics, individual reports, bullwhip analysis, longitudinal tracking)
- Organization branding (logo upload, custom theme colors)
- Completion status management (approved/not approved)
- Exportable reports (PDF, CSV)

**Tier 3 - Class Students ($5 one-time seat):**
- Access via instructor enrollment only
- Multiplayer game sessions with assigned students
- Instructor-configured game parameters (no student modification)
- Turn-based gameplay with real-time status indicators
- In-game chat (if enabled by instructor)
- Player presence indicators
- Automatic AI takeover for inactive players (2-minute threshold)
- AI-generated assessments tailored to multiplayer session
- Pass/fail status based on instructor threshold
- Game history and performance metrics
- Access to game replays and decision history
- Permanent data retention for longitudinal analytics

**Technical Foundation:**
- Next.js frontend with TypeScript and Tailwind CSS
- FastAPI backend with Pydantic AI integration
- Supabase database with Row Level Security
- Stripe payment integration (subscriptions + one-time purchases)
- Supabase Auth for email verification
- SendGrid for transactional emails
- Deployment on Vercel with CI/CD
- Automated testing for core game logic
- API documentation (OpenAPI/Swagger)

**MVP Success Criteria:**
1. Free users can complete 20-week demo game with AI opponents
2. Paid Students can configure and complete 20-52 week games with full AI assessments
3. Instructors can purchase seats, enroll 30+ students, auto-allocate to games, and monitor in real-time
4. AI-generated questions accurately reflect supply chain concepts
5. Visualizations clearly display bullwhip effect
6. Payment system processes all transaction types correctly
7. Seat management tracks purchases and prevents reuse
8. Organization branding applies correctly

### Growth Features (Post-MVP, Months 2-6)

**Enhanced Communication:**
- Advanced chat features (@mentions, file sharing)
- In-app notifications system
- Email digest preferences

**Advanced Game Customization:**
- Variable demand patterns (seasonal, trend-based, random shocks)
- Configurable supply chain structures (3-tier, 5-tier)
- Custom cost parameter templates

**Gamification:**
- Global leaderboards (optional participation)
- Achievement badges
- Performance levels and progression system

**Mobile & Accessibility:**
- Progressive Web App (PWA) for offline play
- Mobile phone optimization (<768px screens)
- Full WCAG 2.1 AA compliance

**Advanced Analytics:**
- Predictive performance indicators (mid-game outcome prediction)
- Decision pattern AI analysis beyond post-game insights
- Comparative benchmarking against historical data

**Community Features:**
- Discussion forums
- Best practices library
- Instructor-created scenario sharing (basic)

### Vision (Long-term, 6-12+ Months)

**Enterprise Tier ($299/month):**
- SSO integration (SAML, OAuth)
- Custom domain support
- LMS integration (Canvas, Moodle, Blackboard, LTI)
- Department seat pooling
- Dedicated support

**Platform Expansion:**
- Native mobile apps (iOS/Android)
- Industry-specific simulation scenarios (retail, manufacturing, healthcare)
- Multi-language support and localization
- VR/AR immersive experience

**Educational Ecosystem:**
- Certification program partnered with APICS/CSCMP
- Marketplace for instructor-created scenarios
- AI-powered curriculum development assistance
- Team collaboration mode (multiple students per position)
- Peer review system

**Advanced Features:**
- Detailed game replay with step-by-step visualization
- "What-if" simulator for exploring alternative decisions
- Integration with corporate ERP systems for real-world scenarios
- Research partnerships for supply chain behavior studies

---

## Domain-Specific Requirements: Educational Technology

As an EdTech platform in the higher education and professional training space, the following domain considerations shape all features:

### Privacy and Data Handling
- **User Data Protection**: Secure handling of student performance data, instructor information, and organizational data
- **Data Retention**: Permanent retention of game history for longitudinal analytics (explicit in user agreements)
- **Data Portability**: Students and instructors can export their data (CSV, PDF)
- **Minimal Data Collection**: Only collect data necessary for platform functionality
- **Institutional Responsibility**: Platform supports compliance but ultimate FERPA/COPPA responsibility rests with institutions

### Assessment Validity and Pedagogy
- **Learning Objectives Alignment**: AI-generated assessments must test supply chain concepts (bullwhip effect, inventory management, lead time impacts)
- **Question Quality**: 8-12 questions per game covering multiple cognitive levels (recall, application, analysis)
- **Pedagogical Soundness**: Feedback connects decisions to outcomes, reinforcing learning
- **Instructor Override**: Instructors can review and modify AI assessments to ensure educational quality
- **Fairness**: Multiplayer games use identical configurations for fair comparison

### Accessibility (Basic AA Compliance in MVP)
- **Keyboard Navigation**: All functionality accessible via keyboard
- **Screen Reader Support**: Semantic HTML and ARIA labels
- **Color Contrast**: WCAG 2.1 AA contrast ratios
- **Responsive Design**: Minimum 768px width (desktop/laptop/tablet)
- **Clear Language**: AI-generated content uses clear, professional English appropriate for higher education

### Content Guidelines
- **Professional Tone**: All AI-generated content maintains academic professionalism
- **Age Appropriateness**: Content suitable for college-age and adult learners
- **Bias Mitigation**: AI prompts designed to avoid cultural, gender, or demographic bias
- **Content Moderation**: In-game chat (if enabled) includes basic profanity filtering

---

## Innovation & Novel Patterns

### First-Mover Advantage: AI-Powered Beer Game

**Market Gap Identified:**
No existing Beer Game simulation integrates AI for opponents, assessment generation, and personalized feedback. This represents a genuine competitive moat opportunity with an estimated 6-12 month window before competitors respond.

**Innovation Pattern 1: Realistic AI Opponents**

**What Makes It Unique:**
AI opponents using Gemini 2.5 Pro/Flash don't play optimally - they demonstrate authentic human supply chain behavior patterns:
- **Overreaction to Stockouts**: Panic ordering when inventory runs low
- **Amplification Behavior**: Ordering more than actual demand requires
- **Gradual Adjustment**: Slow adaptation to changing conditions
- **Cognitive Biases**: Anchoring on recent data, loss aversion, recency bias

**Why It Matters:**
Students learn supply chain concepts by observing realistic decision-making patterns, not artificial optimal play. The bullwhip effect emerges naturally from human-like AI behavior.

**Validation Approach:**
- Extensive prompt engineering in Week 1 of development
- Beta testing with supply chain instructors to validate realism
- Comparison against historical human Beer Game data
- Iterative refinement based on educational effectiveness
- Fallback to rule-based AI if LLM consistency falls below 95%

**Innovation Pattern 2: Context-Aware AI Assessments**

**What Makes It Unique:**
AI-generated assessments are personalized to each student's specific gameplay:
- Questions reference actual decisions made in specific rounds
- Feedback connects those decisions to observed outcomes
- Difficulty adapts based on game performance
- Multiple question types test different cognitive levels

**Example:**
"In round 7, you ordered 15 units when your backlog was only 8. How did this decision contribute to the bullwhip effect you observed in rounds 10-12?"

**Why It Matters:**
Generic assessments test theory. Personalized assessments test understanding by forcing students to reflect on their own decisions and consequences.

**Validation Approach:**
- Instructor review and override capability
- Target 4.0+ out of 5.0 relevance rating
- Beta testing with 20+ students
- Continuous refinement based on feedback
- Weighted scoring ensures fair grading

**Innovation Pattern 3: Automated Classroom Orchestration**

**What Makes It Unique:**
First platform to fully automate Beer Game classroom management:
- Automated student allocation to multiplayer games (1-4 per game)
- Real-time monitoring dashboard for all active games
- AI-generated assessments for entire class simultaneously
- Longitudinal analytics tracking student performance across semesters

**Why It Matters:**
Transforms instructors from game administrators to learning facilitators, saving 5+ hours per class while improving learning outcomes.

**Validation Approach:**
- Beta testing with 5+ instructors
- Time-tracking studies comparing traditional vs. automated administration
- Instructor satisfaction surveys
- Iteration based on usability feedback

### Technical Innovation

**Provider-Agnostic AI Architecture:**
Using Pydantic AI enables switching between LLM providers (Gemini, OpenAI, Anthropic) without code changes, protecting against:
- API cost increases
- Service availability issues
- Model quality degradation
- Vendor lock-in

**Real-Time Multi-Tenant Multiplayer:**
Supabase Realtime + Row Level Security enables secure, scalable real-time multiplayer without complex WebSocket infrastructure.

---

## Functional Requirements

Requirements are organized by capability area, connecting to user value and the platform's dual magic: AI intelligence and instructor automation.

### FR-1: User Management & Authentication

**FR-1.1: User Registration**
- Users register with email and password
- Email verification required before platform access
- CAPTCHA protection on registration form to prevent bot abuse
- Account creation supports all four tiers (Free, Paid Student, Paid Instructor, Class Student)
- **User Value**: Secure, spam-free platform entry
- **Acceptance Criteria**: User receives verification email within 60 seconds, CAPTCHA blocks 95%+ bot attempts

**FR-1.2: Authentication & Session Management**
- Secure login with email/password via Supabase Auth
- JWT-based session tokens
- "Remember me" functionality (30-day session)
- Password reset flow with email verification
- Account security settings (password change, email update)
- **User Value**: Secure, persistent access across devices
- **Acceptance Criteria**: Login completes in <2 seconds, password reset email delivered within 60 seconds

**FR-1.3: User Roles & Permissions**
- Four distinct user roles: Free User, Paid Student, Paid Instructor, Class Student
- Users can simultaneously hold multiple roles (e.g., Paid Student AND Class Student)
- Role-based access control enforced at API and UI levels
- **User Value**: Flexible dual-role capability for personal learning and classroom participation
- **Acceptance Criteria**: Users can access features appropriate to each active role, data separation maintained

**FR-1.4: Profile Management**
- Users maintain profile with name, email, organization (optional)
- Instructors configure organization branding (logo upload, custom theme colors)
- Profile data exportable
- **User Value**: Personalization and organizational identity
- **Acceptance Criteria**: Organization branding applies within 5 seconds of save, logo displays correctly across all pages

### FR-2: Subscription & Payment Management

**FR-2.1: Subscription Tiers**
- Three subscription tiers: Free (default), Paid Student ($5/month), Paid Instructor ($29.99/month)
- Stripe integration for payment processing
- Monthly billing with automatic renewal
- Proration for mid-cycle upgrades/downgrades
- **User Value**: Clear pricing, flexible tier selection
- **Acceptance Criteria**: Subscription activation immediate upon payment, billing accurate to the day

**FR-2.2: Seat Purchase System (Instructor Only)**
- Instructors purchase seats for Class Students
- Bulk pricing tiers: 1-25 seats ($5), 26-100 ($4.50), 101-250 ($4), 251+ ($3.50)
- One-time payment per seat via Stripe
- Seat inventory tracking (purchased vs. assigned vs. consumed)
- Non-reusable seats (permanent data retention for longitudinal analytics)
- **User Value**: Cost-effective bulk purchases, clear seat tracking, compliance with "one purchase per student" model
- **Acceptance Criteria**: Bulk discount applied automatically, seat count updates immediately, seats cannot be reassigned after consumption

**FR-2.3: Payment Processing**
- Stripe webhook handling for subscription events (created, renewed, cancelled, failed)
- Failed payment retry logic (3 attempts over 7 days)
- Grace period for failed payments (3 days before downgrade)
- Invoice generation and email delivery
- Payment history accessible to users
- **User Value**: Reliable billing, clear payment history
- **Acceptance Criteria**: Webhooks processed within 5 seconds, failed payments trigger email notification, invoices emailed within 1 hour

**FR-2.4: Subscription Management**
- Users can upgrade/downgrade tiers
- Users can cancel subscriptions (access maintained until period end)
- Refund policy enforced (pro-rated refunds within 7 days)
- Cancellation flow with feedback collection
- **User Value**: Control over subscription, fair refund policy
- **Acceptance Criteria**: Tier changes take effect immediately, cancellation preserves access until period end

### FR-3: Beer Game Core Engine

**FR-3.1: Supply Chain Simulation Logic**
- Four-echelon supply chain: Retailer → Wholesaler → Distributor → Factory
- Weekly turn-based gameplay (20-52 weeks configurable)
- Order placement and fulfillment with configurable lead times (default: 2-week shipping, 2-week production)
- Inventory tracking (on-hand, in-transit, backlog)
- Cost calculation (holding cost default $0.50/unit/week, backlog cost default $1.00/unit/week)
- Demand pattern generation (fixed or variable based on configuration)
- Information visibility (full or limited based on configuration)
- **User Value**: Accurate simulation of Beer Game dynamics, bullwhip effect emerges naturally
- **Acceptance Criteria**: Game logic matches MIT Beer Game rules, bullwhip effect demonstrable across all difficulty levels

**FR-3.2: Game Configuration (Paid Students & Instructors)**
- Duration: 20-52 weeks
- Cost parameters: Holding cost, backlog cost (per unit per week)
- Lead times: Shipping delay, production delay (in weeks)
- Difficulty levels: Easy, Medium, Hard (affects initial conditions and demand variability)
- Information visibility: Full (see all echelons) or Limited (see only own position)
- Initial inventory: Configurable starting inventory for each position
- **User Value**: Customizable learning experience, test different scenarios
- **Acceptance Criteria**: All parameters saved with game configuration, game behavior reflects selected parameters

**FR-3.3: Game State Management**
- Real-time game state persistence (every action saved immediately)
- Pause/Resume with timestamp tracking functionality (Paid Students or instructors only)
- Game state includes all necessary data to continue a paused game, for instance: current week, all orders, inventory levels, costs, player decisions
- State synchronization for multiplayer games
- **User Value**: Never lose progress, resume games across sessions
- **Acceptance Criteria**: Game state updates <500ms, resume loads exact state from save point, no data loss on disconnect

**FR-3.4: Turn Processing**
- Player order entry (numeric input with validation)
- AI opponent move generation (asynchronous)
- Each order from all the players must have been registered before the turn processing can start
- Each human player (most single and multiplayer games), must be able to track who has sent their order and who has not sent their order
- When an order is registered, it cannot be undone
- Turn completion triggers state updates (fir instance orders fulfilled, shipments arrive, costs accrue, metrics, statistics etc)
- When turn is triggered, users see an animation resembling the movement of pieces on a board
- Turn history recorded for analysis
- **User Value**: Smooth turn progression, clear feedback on decisions
- **Acceptance Criteria**: Turn processing completes within 10 seconds, all state updates atomic (no partial turns)

### FR-4: AI Integration

**FR-4.1: AI Opponent System**
- Two AI quality tiers: Gemini Flash (Free), Gemini Pro (Paid)
- AI opponents demonstrate realistic supply chain behavior (overreaction, gradual adjustment, cognitive biases)
- The AI must not know that its playing a game
- The AI has the exact same game information as a human player
- AI decision-making considers: current inventory, recent orders, perceived demand, position-specific constraints
- Fallback to rule-based AI if LLM fails after a certain number of retries (95% uptime requirement)
- **User Value**: Realistic gameplay against human-like opponents, educational bullwhip effect demonstration
- **Magic Moment**: AI opponents make the same mistakes humans make, teaching supply chain psychology
- **Acceptance Criteria**: AI opponents produce bullwhip effect 90%+ of games, decision consistency 95%+, response time <3 seconds per turn

**FR-4.2: AI Assessment Generation**
- Generate 8-12 questions per game covering supply chain concepts. This number should be configurable by the instructor.
- Question types: Multiple choice (4 options), short text (1-2 sentences), long text (paragraph), numeric (calculations)
- Questions personalized to player's specific decisions and game outcomes
- Question distribution: 40% multiple choice, 30% short text, 20% long text, 10% numeric. These values should be configurable by the instructor
- Cognitive levels: 30% recall, 40% application, 30% analysis. These values should be configurable by the instructor.
- **User Value**: Personalized assessments test understanding, not memorization
- **Magic Moment**: Questions like "In round 7, you ordered 15 units when your backlog was only 8. How did this decision contribute to the bullwhip effect?"
- **Acceptance Criteria**: Assessments generated within 10 seconds, questions reference actual gameplay, relevance rating 4.0+ out of 5.0

**FR-4.3: AI Feedback & Scoring**
- Automated grading using AI for text responses, rule-based for multiple choice/numeric
- Weighted scoring: Multiple choice (1 point), short text (2 points), long text (3 points), numeric (2 points). These numbers should be configurable by the instructor.
- Instant feedback with explanations connecting decisions to outcomes
- Pass/fail determination based on configurable threshold (default 70%). Instructor should be able to switch to grades A, B, C, D, E and F based on points earned and grade intervals.
- Instructor review and override capability
- Instructor can add suggested answers to short and long text questions for AI to use when grading and giving feedback
- **User Value**: Instant, detailed feedback reinforcing learning
- **Acceptance Criteria**: Scoring completes within 10 seconds, feedback explains concepts clearly, grading accuracy 85%+ matches instructor review

**FR-4.4: AI Cost Management**
- Tier-based AI model selection (Flash for Free, Pro for Paid)
- Caching of common AI responses
- Rate limiting on free tier (3 games/day) to control costs
- Usage monitoring and alerting
- **User Value**: Sustainable AI costs enable affordable pricing
- **Acceptance Criteria**: AI costs <20% of revenue (Free), <15% (Paid), caching reduces API calls by 30%+

### FR-5: Single-Player Game Experience (Tiers 0 & 1)

**FR-5.1: Game Dashboard**
- Current game status: Week number, position, inventory levels, costs, statistics, metrics and full history
- Game flow board imitating a physical game board
- Order entry interface with validation (0-> units)
- Real-time visualization of inventory, costs, orders over time (Recharts)
- Turn history table showing past decisions
- Turn processing happens when user and all AI players have submitted their orders successfully.
- Game controls: Send order, Pause/Save (Paid only), Leave Game. Leaving a game set up by instructor with grading, will result in a not passed/F.
- Animation during turn processing
- **User Value**: Clear game state visibility, easy decision-making
- **Acceptance Criteria**: Dashboard loads in <2 seconds, visualizations update in real-time, validation prevents invalid orders

**FR-5.2: Game Flow**
- Role selection: Choose one of four positions (Retailer, Wholesaler, Distributor, Factory)
- Game initialization with configured parameters
- Turn-based progression (player sends order → AI opponents play → turn advances)
- The user sees live when the other players have successfully sent orders.
- Game completion after configured weeks
- Post-game summary
- **User Value**: Structured gameplay flow, clear progression
- **Acceptance Criteria**: Game completes all weeks without errors, post-game summary displays within 3 seconds

**FR-5.3: Visualizations & Analytics**
- Real-time charts: Inventory over time, costs over time, orders vs. demand, bullwhip effect diagram
- Post-game analysis: Total cost, final inventory, cost breakdown (holding vs. backlog), performance metrics
- Decision pattern insights (AI-generated) for Paid Students
- Comparison to optimal play (Paid Students)
- **User Value**: Understand supply chain dynamics visually, identify improvement areas
- **Magic Moment**: Watching the bullwhip effect emerge in real-time visualization
- **Acceptance Criteria**: Charts update within 500ms, post-game analysis loads within 5 seconds, insights relevant to gameplay

**FR-5.4: Game History (Paid Students)**
- Personal game history accessible from dashboard
- Filter and sort by date, score, difficulty and other configuration parameters
- Replay capability (view past games turn-by-turn)
- Delete games from history
- Export game report (pdf)
- Export game data (excel)
- **User Value**: Track improvement over time, review past decisions
- **Acceptance Criteria**: History loads within 2 seconds, export includes all game data

**FR-5.5: Rate Limiting (Free Tier)**
- 3 games per day limit
- 1 concurrent game limit
- Clear messaging when limits reached
- Upgrade prompt when hitting limits
- **User Value**: Fair free tier prevents abuse while encouraging upgrades
- **Acceptance Criteria**: Limits enforced server-side, upgrade prompt displays when limit reached

### FR-6: Multiplayer Game Experience (Tier 3 - Class Students)

**FR-6.1: Multiplayer Game Sessions**
- 1-4 players per game (instructor-configured)
- Each player assigned one position (Retailer, Wholesaler, Distributor, Factory)
- Turn-based synchronous gameplay (all players submit orders before turn advances)
- Real-time presence indicators (online/offline, active/idle)
- Game proceeds only when all players (or AI replacements) successfully have submitted their orders
- **User Value**: Collaborative learning with peers, realistic multi-party supply chain
- **Acceptance Criteria**: Games support 4 concurrent players, presence updates within 2 seconds, turn synchronization accurate

**FR-6.2: Player Activity Management**
- AFK detection: 2-minute timer per turn, configurable by instructor
- Warning at 30 seconds remaining
- Option to temporarily ley AI takeover after 2 minutes (AI submits order for inactive player), configurable by instructor. If grading, the student will get not passed/F, if too many of the steps were taken by AI. The threshold is set by the instructor.
- "Nudge" feature to notify inactive players
- Manual instructor intervention capability (Classroom mode)
- Consensual "Pause & Save" feature (all players must agree)
- **User Value**: Games complete even with inactive players, fair progression
- **Acceptance Criteria**: AFK timer accurate to second, AI takeover seamless, nudge notification delivered within 5 seconds

**FR-6.3: In-Game Communication**
- This is a multi player feature
- Text chat channels in the game:
  - between players within the same role, always activated, no configuration
  - between players with adjacent roles, configurable by instructor, off by default
  - between player and AI
  - between player and instructor
- Basic profanity filtering
- Chat history persisted with game
- Instructor can disable chat per game
- **User Value**: Coordination and discussion during gameplay
- **Acceptance Criteria**: Messages delivered within 2 seconds, profanity filter catches common terms

**FR-6.4: Multiplayer Assessment**
- AI assessments tailored to each player's role and decisions
- Individual grading based on position-specific performance
- Pass/fail status or grade based on instructor threshold
- Resubmission capability with limits (configurable by instructor)
- **User Value**: Fair assessment of individual contribution in team setting
- **Acceptance Criteria**: Assessments reflect role-specific decisions, grading accounts for position differences

### FR-7: Instructor Classroom Management (Tier 2)

**FR-7.1: Class Creation & Management**
- Create unlimited classes with name, description, semester/term
- Each class has unique identifier
- Archive/delete classes
- View class roster and game assignments
- **User Value**: Organize multiple courses/sections
- **Acceptance Criteria**: Class creation completes in <2 seconds, all classes accessible from dashboard

**FR-7.2: Student Enrollment**
- Bulk enrollment via CSV import (columns: name, email)
- Manual individual student entry
- CSV validation (email format, duplicate detection)
- Automatic email invitation to enrolled students
- Student removal (with or without seat refund)
- **User Value**: Rapid enrollment of large classes (30+ students in minutes)
- **Magic Moment**: Upload CSV, click enroll, 30 students invited in <1 minute
- **Acceptance Criteria**: CSV import handles 100+ students, validation catches errors, email invitations sent within 5 minutes

**FR-7.3: Game Allocation**
- Automated allocation: System assigns students to games (1-4 per game)
- Manual override: Instructor can adjust allocations
- Common game configuration applied to all games (duration, costs, difficulty)
- Fairness ensured through identical parameters
- Allocation preview before confirmation
- **User Value**: Instant game setup for entire class, fair comparison
- **Acceptance Criteria**: Allocation completes in <5 seconds for 100 students, manual adjustments supported

**FR-7.4: Real-Time Monitoring Dashboard**
- View all active games in class simultaneously
- Game status indicators: Not started, In progress (week X/Y), Completed
- Quick metrics per game: Current week, total costs, player activity
- Drill-down to individual game details
- Refresh rate: 5 seconds (configurable)
- Class metrics, across all games
- **User Value**: At-a-glance class progress, identify struggling students
- **Acceptance Criteria**: Dashboard loads within 3 seconds, displays 50+ games, updates every 5 seconds

**FR-7.5: Class-Wide Controls**
- Pause All Games: Pauses all active games in class
- Resume All Games: Resumes all paused games
- Reset All Games: Resets all games to week 1 (confirmation required)
- Send Message to All: Broadcast message to all students
- **User Value**: Classroom management efficiency, handle disruptions
- **Acceptance Criteria**: Class-wide actions complete within 10 seconds for 50+ games

**FR-7.6: Individual Game Actions**
- View detailed game progress (turn-by-turn history)
- Remove student from game (AI replaces player)
- Send direct message to specific student or role
- Override game configuration (if not yet started)
- **User Value**: Handle individual student issues without disrupting class
- **Acceptance Criteria**: Game details load within 2 seconds, student removal immediate

**FR-7.7: Assessment Management**
- Configure assessment threshold (default 70% pass or grade thresholds)
- Configure exercises, levels, topics etc, changing the system prompts.
- Review AI-generated assessments before student access (optional)
- Override AI grading (change score or pass/fail status)
- Configure resubmission limits (default: 2 attempts)
- Bulk approve/reject students
- **User Value**: Instructor control over grading standards, quality assurance
- **Acceptance Criteria**: Grade overrides save immediately, resubmission limits enforced, bulk actions complete within 5 seconds for 50+ students

**FR-7.8: Communication System**
- Broadcast messages to all class students (email + in-app notification)
- Direct messages to individual students
- Message templates for common scenarios (game start reminder, deadline reminder)
- Message history accessible
- **User Value**: Efficient communication with students
- **Acceptance Criteria**: Messages delivered within 5 minutes, templates save time

### FR-8: Analytics & Reporting

**FR-8.1: Class Analytics Dashboard (Instructors)**
- Class-wide metrics: Average total cost, completion rate, pass rate, average score
- Distribution charts: Cost distribution, score distribution
- Bullwhip effect analysis: Average amplification ratio across class
- Individual student reports: Performance summary, game history, assessment scores
- Longitudinal tracking: Compare cohorts across semesters
- **User Value**: Identify trends, measure learning outcomes, inform teaching
- **Acceptance Criteria**: Dashboard loads within 5 seconds, all charts interactive, longitudinal data accurate

**FR-8.2: Exportable Reports**
- Export formats: PDF (formatted reports), CSV (raw data)
- Class summary report (PDF): Class metrics, top performers, struggling students
- Individual student reports (PDF): Game summary, assessment results, recommendations
- Raw data export (CSV): All game data, all assessment data
- **User Value**: Integration with institutional systems, record-keeping
- **Acceptance Criteria**: PDF reports professional quality, CSV exports include all fields

**FR-8.3: Student Performance Tracking**
- Personal dashboard showing game history and scores
- Progress over time (if multiple games completed)
- Performance metrics: Average total cost, best game, improvement rate
- **User Value**: Self-assessment, motivation through progress tracking
- **Acceptance Criteria**: Dashboard loads within 2 seconds, metrics accurate

### FR-9: Organization Branding (Instructors)

**FR-9.1: White-Label Customization**
- Upload organization logo (max 2MB, PNG/JPG/SVG)
- Configure custom theme colors (primary, secondary, accent)
- Branding applies to: Instructor dashboard, student game interface, emails, reports
- Preview branding before applying
- Revert to default branding option
- **User Value**: Institutional credibility, professional appearance
- **Acceptance Criteria**: Logo uploads within 5 seconds, theme colors apply immediately, branding consistent across all pages

### FR-10: Data Management & Compliance

**FR-10.1: Data Retention**
- Permanent retention of game history for longitudinal analytics (explicit in user agreement)
- Instructor access to historical data across semesters
- Student access to personal game history indefinitely (as long as account exists)
- Deleted accounts trigger data anonymization (PII removed, gameplay data retained for research)
- **User Value**: Long-term learning analytics, research capability
- **Acceptance Criteria**: Historical data queryable for 5+ years, anonymization completes within 24 hours

**FR-10.2: Data Export & Portability**
- Students can export all personal data (JSON format)
- Instructors can export all class data (CSV/PDF)
- GDPR-compliant data export (delivered within 30 days of request)
- **User Value**: Data ownership, compliance with privacy regulations
- **Acceptance Criteria**: Export completes within 5 minutes, includes all user data

**FR-10.3: Account Deletion**
- Users can request account deletion
- 7-day grace period before permanent deletion
- PII removed, gameplay data anonymized
- Confirmation email sent
- **User Value**: Privacy control
- **Acceptance Criteria**: Deletion request triggers email within 1 hour, PII removed after 7 days

---

## Non-Functional Requirements

### NFR-1: Performance

**NFR-1.1: Application Load Time**
- Landing page loads in <2 seconds on standard broadband (25 Mbps)
- Game dashboard loads in <3 seconds with full game state
- Instructor monitoring dashboard loads in <5 seconds with 50+ active games
- **Rationale**: Fast load times critical for user engagement and classroom efficiency
- **Measurement**: Vercel analytics, Lighthouse scores targeting 90+ performance score

**NFR-1.2: API Response Time**
- 95th percentile API response time <200ms for read operations
- 95th percentile API response time <500ms for write operations
- Game state updates processed in <500ms
- AI opponent move generation <3 seconds per turn
- **Rationale**: Responsive gameplay maintains learning engagement
- **Measurement**: API monitoring, response time logging

**NFR-1.3: Real-Time Update Latency**
- Multiplayer game state updates delivered to all players within 2 seconds
- Presence indicators update within 2 seconds of player status change
- Instructor dashboard refreshes every 5 seconds (configurable)
- **Rationale**: Real-time awareness critical for multiplayer coordination and instructor monitoring
- **Measurement**: Supabase Realtime latency monitoring

**NFR-1.4: Visualization Rendering**
- Charts and graphs render in <500ms after data fetch
- Chart interactions (zoom, pan, hover) respond within 100ms
- Real-time chart updates during gameplay <1 second lag
- **Rationale**: Smooth visualizations enhance understanding of supply chain dynamics
- **Measurement**: Browser performance profiling

### NFR-2: Security

**NFR-2.1: Authentication & Authorization**
- JWT-based authentication with secure token storage
- Row Level Security (RLS) enforced on all database tables
- Role-based access control (RBAC) at API and UI levels
- Password requirements: Minimum 8 characters, complexity enforced
- Session timeout: 30 days for "remember me", 24 hours without
- **Rationale**: Protect user data and prevent unauthorized access
- **Compliance**: OWASP authentication best practices

**NFR-2.2: Data Encryption**
- Data encrypted in transit (TLS 1.3)
- Data encrypted at rest (Supabase default encryption)
- Sensitive data (payment info) never stored; Stripe handles PCI compliance
- JWT tokens include expiration and signature verification
- **Rationale**: Protect sensitive educational and payment data
- **Compliance**: PCI DSS (via Stripe), general data protection best practices

**NFR-2.3: Input Validation & Sanitization**
- Server-side validation on all API endpoints
- SQL injection prevention via parameterized queries (SQLAlchemy ORM)
- XSS prevention via input sanitization and Content Security Policy
- CSRF protection via SameSite cookies and token validation
- Rate limiting on authentication endpoints (5 attempts per 15 minutes)
- **Rationale**: Prevent common web vulnerabilities (OWASP Top 10)
- **Compliance**: OWASP security standards

**NFR-2.4: Payment Security**
- Stripe integration for PCI DSS compliance
- No credit card data stored on platform servers
- Webhook signature verification for all Stripe events
- Secure handling of subscription and payment state
- **Rationale**: Payment security critical for user trust and legal compliance
- **Compliance**: PCI DSS Level 1 (via Stripe)

**NFR-2.5: Privacy & Data Protection**
- Minimal data collection (only necessary fields)
- User consent for data retention explicit in terms
- Data export capability (GDPR Article 20 compliance)
- Account deletion with PII anonymization (GDPR Article 17 compliance)
- No sharing of user data with third parties (except payment processing)
- **Rationale**: User privacy and regulatory compliance
- **Compliance**: GDPR (for EU users), general privacy best practices

### NFR-3: Scalability

**NFR-3.1: Concurrent Users**
- Support 100+ concurrent users without performance degradation
- Support 50+ simultaneous game sessions
- Support 10+ instructors with 30+ students each (300+ total Class Students)
- **Rationale**: Accommodate multiple instructors running classes simultaneously
- **Measurement**: Load testing with K6 or Artillery

**NFR-3.2: Database Scalability**
- Proper indexing on high-query tables (users, games, game_rounds)
- Query performance <100ms for indexed lookups
- Pagination on large result sets (game history, student lists)
- Database connection pooling to handle concurrent requests
- **Rationale**: Maintain performance as data volume grows
- **Measurement**: Database query analysis, Supabase performance monitoring

**NFR-3.3: AI API Scalability**
- Queue-based AI request handling for load balancing
- Retry logic for failed AI API calls (3 attempts with exponential backoff)
- Fallback to rule-based AI if LLM provider unavailable
- Caching of common AI responses (30% API call reduction target)
- **Rationale**: Manage AI costs while maintaining reliability
- **Measurement**: AI API usage monitoring, cache hit rate

**NFR-3.4: Horizontal Scalability**
- Stateless backend API design enabling multiple instances
- Frontend deployed via Vercel edge network for global distribution
- Database and storage externalized (Supabase managed)
- **Rationale**: Scale to support growth without architecture changes
- **Measurement**: Deployment configuration, load balancer metrics

### NFR-4: Reliability & Availability

**NFR-4.1: System Uptime**
- Target 99% uptime during operating hours (defined as 24/7)
- Planned maintenance window: Sunday 2-4 AM EST (maximum 2 hours/month)
- Graceful degradation: Core gameplay functions even if analytics fail
- **Rationale**: Educational platform must be available when instructors schedule classes
- **Measurement**: Uptime monitoring (UptimeRobot or similar), incident tracking

**NFR-4.2: Error Handling & Recovery**
- Automatic retry for transient failures (network, API timeouts)
- User-friendly error messages (no stack traces exposed)
- Error logging and alerting for critical failures
- Game state recovery from last saved point (no data loss)
- **Rationale**: Minimize user impact from technical issues
- **Measurement**: Error rate monitoring, user-reported issues

**NFR-4.3: Data Durability**
- Database backups: Daily automated backups (Supabase managed)
- Point-in-time recovery capability (7 days)
- Game state saved after every action (no progress lost)
- Backup verification (monthly restore tests)
- **Rationale**: Protect educational data and user progress
- **Measurement**: Backup success rate, recovery time objectives (RTO <4 hours)

**NFR-4.4: Disaster Recovery**
- Recovery Time Objective (RTO): 4 hours
- Recovery Point Objective (RPO): 1 hour (maximum data loss)
- Disaster recovery plan documented and tested quarterly
- Geographic redundancy via Supabase and Vercel infrastructure
- **Rationale**: Business continuity in case of major failures
- **Measurement**: DR drill results, incident postmortems

### NFR-5: Usability

**NFR-5.1: User Experience**
- Intuitive interface requiring <5 minutes training for Free/Paid Student tiers
- Instructor dashboard learnable in <15 minutes (with documentation)
- Consistent UI patterns across all pages (design system enforced)
- Clear error messages with actionable guidance
- Help documentation accessible from all pages
- **Rationale**: Low learning curve critical for educational adoption
- **Measurement**: User testing, time-to-first-game metrics

**NFR-5.2: Accessibility (WCAG 2.1 AA)**
- Keyboard navigation for all functionality
- Screen reader support (semantic HTML, ARIA labels)
- Color contrast ratios meet AA standards (4.5:1 for normal text, 3:1 for large text)
- Focus indicators visible on all interactive elements
- Alt text for all images and icons
- **Rationale**: Inclusive design ensures accessibility for all learners
- **Compliance**: WCAG 2.1 AA (MVP), AAA (post-MVP goal)
- **Measurement**: Automated accessibility testing (axe DevTools), manual screen reader testing

**NFR-5.3: Responsive Design**
- Minimum supported screen width: 768px (tablets and up)
- Optimized layouts for desktop (1920x1080), laptop (1366x768), tablet (768x1024)
- Mobile phone support (<768px) deferred to Growth phase
- Touch-friendly controls on tablet devices
- **Rationale**: Focus on primary use case (classroom and study environments)
- **Measurement**: Cross-device testing, browser compatibility matrix

**NFR-5.4: Browser Compatibility**
- Support for modern browsers: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- No Internet Explorer support
- Progressive enhancement approach (core functionality works without JavaScript)
- **Rationale**: Focus on modern browsers reduces development complexity
- **Measurement**: Browser testing matrix, analytics on browser usage

### NFR-6: Maintainability & Testability

**NFR-6.1: Code Quality**
- TypeScript strict mode enabled (frontend and backend types)
- Code coverage: 80%+ for core game logic
- Linting enforced (ESLint, Prettier)
- Code review required for all changes
- **Rationale**: Maintainable codebase for 5-week development timeline
- **Measurement**: Test coverage reports, code quality metrics

**NFR-6.2: Testing Strategy**
- Unit tests for game logic, AI prompts, calculation functions
- Integration tests for API endpoints
- End-to-end tests for critical user flows (registration, gameplay, payment)
- Performance testing for concurrent user scenarios
- **Rationale**: Catch bugs early, ensure quality under load
- **Measurement**: Test suite execution time, bug escape rate

**NFR-6.3: Documentation**
- API documentation via OpenAPI/Swagger
- Code comments for complex logic
- User documentation (getting started, FAQs, video tutorials)
- Instructor onboarding guide
- **Rationale**: Self-service support reduces operational burden
- **Measurement**: Documentation coverage, support ticket reduction

**NFR-6.4: Monitoring & Observability**
- Application performance monitoring (Vercel analytics)
- Error tracking and alerting (Sentry or similar)
- Usage analytics (game starts, completions, conversions)
- AI API cost tracking
- Database performance monitoring (Supabase dashboard)
- **Rationale**: Proactive issue detection, data-driven optimization
- **Measurement**: Mean time to detection (MTTD), mean time to resolution (MTTR)

### NFR-7: Cost Efficiency

**NFR-7.1: Infrastructure Costs**
- Monthly infrastructure budget: <$100 for first 100 users
- Target gross margin: >60% after infrastructure and AI costs
- Cost per user: <$2/month (infrastructure + AI)
- **Rationale**: Sustainable unit economics critical for business viability
- **Measurement**: Monthly cost breakdown, cost per active user

**NFR-7.2: AI Cost Management**
- AI costs <20% of revenue for Free tier
- AI costs <15% of revenue for Paid tiers
- Caching reduces API calls by 30%+
- Model selection based on tier (Flash for Free, Pro for Paid)
- **Rationale**: AI differentiation must be cost-effective
- **Measurement**: AI API usage tracking, cost per assessment/game

---

## Implementation Planning

### Development Approach

**Timeline:** 5 weeks using BMAD methodology (AI-assisted development)
**Track:** BMad Method (greenfield)
**Architecture:** Next.js + FastAPI + Supabase + Pydantic AI

### Required Next Steps

**1. Epic Breakdown (REQUIRED)**

This PRD contains comprehensive requirements covering 10 functional requirement categories and 7 non-functional requirement categories. These must be decomposed into implementable epics and bite-sized stories optimized for 200k context development agents.

**Run:** `workflow create-epics-and-stories` OR `/bmad:bmm:workflows:create-epics-and-stories`

**2. Architecture Design (RECOMMENDED)**

While technical stack is defined (Next.js, FastAPI, Supabase, Pydantic AI), detailed architecture decisions are needed for:
- Database schema design (12+ tables)
- API endpoint structure and versioning
- AI integration architecture (prompt engineering, caching, fallback)
- Real-time multiplayer architecture (Supabase Realtime + RLS)
- Payment integration flow (Stripe webhooks)
- Security architecture (JWT, RBAC, RLS, input validation)

**Run:** `workflow create-architecture` OR `/bmad:bmm:workflows:architecture`

**3. UX Design (RECOMMENDED)**

Platform includes multiple complex interfaces requiring UX design:
- Student game dashboard (real-time gameplay, visualizations)
- Instructor monitoring dashboard (50+ games simultaneously)
- Assessment interface (question types, feedback display)
- Class management interface (enrollment, allocation, analytics)
- Organization branding customization

**Run:** `workflow create-ux-design` OR `/bmad:bmm:workflows:create-ux-design`

**4. Solutioning Gate Check (REQUIRED before development)**

Before proceeding to Phase 4 (Implementation), validate that PRD, architecture, and stories are complete and aligned.

**Run:** `workflow solutioning-gate-check` OR `/bmad:bmm:workflows:solutioning-gate-check`

### Project Track & Epic Strategy

**Track:** BMad Method - Comprehensive planning for complex greenfield project

**Epic Organization Strategy:**
Given the scope, epics should be organized by:
1. **Foundation Epics**: Authentication, database, core infrastructure
2. **Game Engine Epics**: Beer Game logic, AI integration, game state management
3. **Student Experience Epics**: Single-player, multiplayer, assessments, visualizations
4. **Instructor Experience Epics**: Class management, monitoring, analytics, branding
5. **Payment & Subscription Epics**: Stripe integration, tier management, seat purchasing
6. **Polish & Launch Epics**: Testing, documentation, deployment

Each epic should contain 5-10 stories, each story completable in 1-3 hours.

---

## References

**Product Brief:** docs/product-brief-beergame-2025-11-13.md

**Brainstorming Sessions:**
- docs/brainstorming-session-results-2025-10-27.md (Edge cases, AFK handling, CSV validation)

**Technical Research:**
- docs/research-technical-2025-10-27.md (Pydantic AI selection, LLM orchestration)

**Workflow Status:**
- docs/bmm-workflow-status.yaml (Project tracking)

---

## PRD Summary

This Product Requirements Document defines the **Beer Game Interactive Platform**, an AI-powered educational SaaS platform revolutionizing supply chain management education.

**What Makes It Special:**
- **AI Intelligence**: Realistic AI opponents demonstrating human supply chain behavior + personalized AI-generated assessments
- **Instructor Liberation**: 5+ hours saved per class through automated enrollment, allocation, monitoring, and assessment

**Scope:**
- **Four user tiers** delivering complete value proposition (Free Demo, Paid Student, Paid Instructor, Class Student)
- **10 functional requirement categories** with 70+ specific requirements
- **7 non-functional requirement categories** covering performance, security, scalability, reliability, usability, maintainability, and cost efficiency
- **EdTech domain compliance**: Privacy, assessment validity, accessibility (WCAG 2.1 AA)
- **First-mover advantage**: First AI-powered Beer Game simulation in market

**Technical Foundation:**
- Next.js 14+ (TypeScript, Tailwind CSS, Shadcn UI)
- FastAPI (Python, Pydantic AI, SQLAlchemy)
- Supabase (PostgreSQL, Auth, Realtime, RLS)
- Gemini 2.5 Pro/Flash (AI opponents and assessments)
- Stripe (payment processing)
- Vercel (deployment)

**Success Metrics:**
- Break-even within 3-4 months ($550 MRR + seat revenue)
- 10+ instructor subscribers, 50+ student subscribers
- 4.0+ out of 5.0 AI assessment relevance rating
- 80%+ student understanding improvement
- 99% uptime, <3s load times, 100+ concurrent users

**Next Steps:**
1. **Epic & Story Breakdown** (REQUIRED)
2. **Architecture Design** (RECOMMENDED)
3. **UX Design** (RECOMMENDED)
4. **Solutioning Gate Check** (REQUIRED before development)

---

_This PRD captures the complete vision for the Beer Game Interactive Platform, transforming a 60-year-old supply chain simulation into an AI-powered educational revolution._

_The dual magic — AI intelligence that feels human + instructor automation that reclaims time — is woven throughout every requirement, ensuring the platform delivers on its promise to make supply chain education accessible, effective, and scalable._

_Created through collaborative discovery between BIP (Product Owner) and John (AI Product Manager) on 2025-11-13._
