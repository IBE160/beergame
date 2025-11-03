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
*   **FR010: Teacher Authentication:** The system shall allow teachers to register and authenticate using an institutional email.
*   **FR011: Subscription Management:** The system shall provide subscription-based access for teachers, including payment processing.
*   **FR012: Class Management:** The system shall allow teachers to create, manage, and configure classes, including bulk student registration and automated/manual game allocation.
*   **FR013: Common Game Settings:** The system shall enforce common game settings for all students within a class to enable comparative analysis.
*   **FR014: Real-time Class Monitoring:** The system shall provide teachers with a real-time monitoring dashboard for active sessions, student progress, and controls to pause/reset games or replace students with AI.
*   **FR015: AI-Generated Assessment System:** The system shall automatically generate tailored assessments (MCQ, short/long text, numeric) for students, with AI-powered grading and feedback.
*   **FR016: Messaging System:** The system shall enable teachers to broadcast messages to a class or send individual messages to students.
*   **FR017: Analytics Dashboard (Educator):** The system shall provide teachers with an analytics dashboard for class-wide metrics, individual reports, bullwhip analysis, and exportable reports.
*   **FR018: Completion Status Management:** The system shall allow teachers to manage and toggle student completion statuses.

### Non-Functional Requirements

{{non_functional_requirements}}

---

## User Journeys

{{user_journeys}}

---

## UX Design Principles

{{ux_principles}}

---

## User Interface Design Goals

{{ui_design_goals}}

---

## Epic List

{{epic_list}}

> **Note:** Detailed epic breakdown with full story specifications is available in [epics.md](./epics.md)

---

## Out of Scope

{{out_of_scope}}
