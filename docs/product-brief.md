# Product Brief: Beer Game - Interactive Supply Chain Management Simulation Platform

## Case Title
Beer Game: Interactive Supply Chain Management Simulation Platform

## Background
The Beer Game, an MIT-developed simulation, effectively demonstrates supply chain principles like the bullwhip effect. Existing digital versions are often proprietary, expensive, or lack modern features. This project addresses the need for an accessible, feature-rich web platform with AI-assisted learning and comprehensive analytics for both individual learners and educational institutions.

## Purpose
To create an AI-enhanced web-based Beer Game platform that provides:
1. An engaging single-player and multiplayer simulation for individuals to learn supply chain management.
2. A complete classroom management system for educators, including automated student allocation, progress tracking, AI-generated assessments, and detailed analytics.
The goal is to make supply chain education more accessible, interactive, and measurable, leveraging AI to enhance learning outcomes and teaching efficiency.

## Target Users
**Primary Users:**
- Students (supply chain, operations, business administration)
- Supply chain professionals
- Individual learners

**Secondary Users:**
- Educators (operations, supply chain management)
- Corporate training coordinators
- Researchers

## Core Functionality

### Must Have (MVP)

**For Players:**
- User registration and authentication.
- Single-player mode with AI-controlled partners.
- Multiplayer mode with human or AI partners.
- Game configuration: duration, costs, lead times, difficulty, communication visibility.
- Interactive real-time game dashboard: inventory, backorders, orders, shipments, costs, week indicator, order placement.
- AI-powered opponents (LLM API).
- Real-time data visualization: inventory, orders, costs.
- AI-generated game completion summary: performance, insights, educational content, bullwhip visualization.
- Game state persistence.
- Responsive design (desktop, tablet).

**For Educators:**
- Teacher registration and authentication (institutional email).
- Subscription-based access.
- Class management dashboard: create/manage classes, bulk student registration, automated/manual game allocation.
- Common game settings for all students in a class for comparative analysis.
- Real-time monitoring: active sessions, student progress, pause/reset games, remove student (replace with AI).
- AI-generated assessment system: tailored questions (MCQ, short/long text, numeric), AI-assessed, weighted scoring, passing threshold.
- Messaging system: broadcast to class, individual student messages.
- Analytics dashboard: class-wide metrics, individual reports, bullwhip analysis, exportable reports.
- Completion status management.

### Nice to Have (Optional Extensions)
- In-game chat.
- Advanced customization: variable demand, custom costs, different product types, custom supply chain configurations.
- Gamification: leaderboards, achievements, rankings.
- Advanced analytics: predictive indicators, decision pattern analysis.
- Mobile app.
- LMS integration (Canvas, Moodle).
- Social sharing.
- Replay and strategy analysis tools.
- Collaborative team mode.
- Multilingual support.

## Data Requirements
- **User Management:** Supabase Auth, User Profiles (student/teacher/individual), Teachers (subscription details).
- **Game Data:** Games (type, config), Game Sessions, Players (role, AI control).
- **Game State:** Game Rounds (week, timestamp), Player States (inventory, backorders, costs, orders).
- **Education System:** Classes, Class Students, Class Games, Assessments (questions, answers, score, feedback), Questions.
- **Payment & Subscriptions:** Subscriptions (plan, status), Payments (amount, transaction).
- **Analytics & Reporting:** Performance Metrics (total cost, bullwhip), Class Analytics.

## User Flows (Summarized)
1.  **Student Playing Single-Player Game:** Registration, game mode selection, configuration, interactive dashboard, real-time monitoring, AI-generated summary.
2.  **Teacher Setting Up Class Game:** Registration/subscription, class creation, student management (bulk/manual), common game configuration, student allocation, real-time monitoring with controls, messaging, AI-generated assessments, analytics.
3.  **Student Completing Assessment:** Email notification, assessment dashboard, answering various question types, AI-generated immediate feedback, approval status, certificate download.
4.  **Individual Learner (Non-Student) Quick Play:** Guest access, simplified game setup, demo gameplay, conversion prompt for registration.
5.  **Teacher Managing Subscription:** Accessing settings, viewing status, upgrading/downgrading, updating payment, viewing invoices, cancellation.
6.  **Student Playing Multiplayer Game:** Game mode selection, host/join game, waiting lobby, turn-based gameplay, real-time state, performance comparison, AI-generated insights.

## Technical Constraints (Summarized)
- **Platform:** Web-based, responsive (desktop, laptop, tablet), minimum 768px width.
- **Performance:** Load <3s, game state updates <500ms, 100 concurrent sessions, DB queries <200ms (95th percentile).
- **Security:** Supabase Auth (JWT, RLS), data encryption, RBAC, PCI DSS (Stripe).
- **Integration:** Supabase (DB, Auth, Realtime), OpenAI API (LLM), Stripe (payments), SendGrid (emails).
- **Data:** Game state persistence, history for analytics, CSV/PDF export, DB backups.
- **Development:** 6-week timeline with AI assistance, automated testing, API documentation.

## Success Criteria
- **Functional:** Full game completion, teacher class management, accurate AI questions, clear bullwhip visualization, successful payment processing.
- **Technical:** 99% uptime, game state persistence, 100 concurrent users, API response <500ms, >80% test coverage.
- **Educational:** 80%+ student understanding improvement, bullwhip effect identification, 5+ hours saved for teachers.
- **Business:** 10+ paying teacher subscribers (3 months), 2+ games/individual learner, 70%+ trial conversion.

## Technical Specifications (Summarized)
- **Frontend:** Next.js 14+ (App Router), TypeScript, Tailwind CSS, Zustand, Recharts, Shadcn UI, React Hook Form, Supabase Auth UI, Supabase Realtime, Axios, Vercel deployment.
- **Backend:** FastAPI (Python), Supabase (PostgreSQL), Supabase Auth, RLS, SQLAlchemy, Alembic, OpenAI GPT-4 API, Stripe API, SendGrid, Pytest, UV, Vercel deployment.
- **Database:** Supabase (PostgreSQL), SQLAlchemy, Alembic, normalized schema, RLS, indexes, JSON/JSONB columns, Supabase Realtime.
- **AI Integration:** Gemini 2.5 pro/flash, Pydantic AI, prompt engineering, rate limiting, caching, fallback logic.
- **Platform Type:** Web application (desktop, laptop, tablet primary).
- **User Authentication:** Supabase Auth (email/password, JWT, email verification, password reset, session management, RBAC).
- **Payment System:** Stripe (subscriptions, pricing tiers, free trial, automatic processing, webhooks, customer portal).

## Timeline and Milestones
**Total Duration:** 5 weeks (BMAD-methodology 4-phase model)
- **Week 44 (Phase 1 & 2: Analyze and Planning):** Requirements, competitive analysis, user research, feature prioritization, risk analysis, project charter.
- **Week 45-46 (Phase 3: Solution Architecture and UI/UX Design):**
    - **Week 45:** Database schema, API design, system architecture, tech stack, AI/Auth/Payment integration, security.
    - **Week 46:** Information architecture, wireframing, high-fidelity mockups, component library, responsive design, user flow diagrams.
- **Week 47-48 (Phase 4: Development and Deployment):**
    - **Week 47 (Sprint 1):** Project initialization, DB setup, authentication, core game logic, AI player integration, game persistence, basic player UI.
    - **Week 48 (Sprint 2 & Launch):** Teacher platform (class management, student import, allocation, monitoring), AI assessment, payment integration, analytics, testing, deployment prep, launch.
- **Post-Launch:** Feedback, bug fixes, performance, feature enhancements, documentation, retrospectives.

## Development Approach
- **AI-Assisted Development:** Claude Code/GitHub Copilot for boilerplate, AI for types/endpoints, human oversight for logic/architecture.
- **Testing:** Unit (game logic), Integration (API), End-to-end (user flows), Manual (AI content), Security, Performance, Cross-browser.
- **Version Control:** Git (feature branch, protected main, semantic versioning).

## Risk Assessment (Summarized)
- **Technical Risks:** AI API costs (mitigation: caching, rate limiting, fallback AI), real-time performance (mitigation: polling, WebSockets, managed services), database performance (mitigation: pagination, archiving, indexing).
- **Project Risks:** Scope creep (mitigation: clear MVP, prioritization), AI integration complexity (mitigation: prompt testing, fallback logic), payment integration (mitigation: Stripe SDKs, dedicated time).
- **User Adoption Risks:** Teacher onboarding (mitigation: clear flow, tutorials), student engagement (mitigation: UI/UX testing, gamification).

## Assumptions
- AI-assisted development increases productivity by 40-50%.
- PostgreSQL + Prisma handles 100 concurrent users.
- OpenAI API maintains availability/performance.
- Stripe handles payment security/compliance.
- Modern browsers support required features.
- Teachers willing to pay $19-99/month.
- 6 weeks sufficient for MVP with AI assistance.
