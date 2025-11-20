# ibe160 UX Design Specification

_Created on 2025-11-13 by BIP_
_Generated using BMad Method - Create UX Design Workflow v1.0_

---

## Executive Summary

**Project:** Beer Game Interactive Platform - AI-powered supply chain education simulation

**Target Experience:**
- **Students:** Fun, excited, in control, curious, determined, and competitive, fostering a sense of learning through engaging gameplay.
- **Instructors:** Simplicity, oversight, and pleased by having engaged students, feeling liberated from administrative tasks.
- **Core Magic:** "Great with AI-driven players and feedback, fun with fellow students"

**Design Inspiration:** Established UX patterns from educational, simulation/strategy game, and productivity/dashboard platforms, focusing on engagement, clear feedback, and efficient oversight.

**User Tiers:**
1. Free Demo Users - Fixed 20-week games with AI opponents
2. Paid Students ($5/month) - Full configuration + AI assessments
3. Paid Instructors ($29.99/month) - Complete classroom management
4. Class Students ($5 one-time) - Multiplayer with classmates

**Platform:** Web application (Next.js + Tailwind + Shadcn), desktop/laptop/tablet focus (≥768px)

---

## 1. Design System Foundation

### 1.1 Design System Choice

**Selected:** Shadcn UI + Tailwind CSS

**Rationale:**
- **Component Library:** Shadcn UI provides unstyled, accessible primitives built on Radix UI
- **Full Customization:** Copy-paste components into codebase, full ownership and control
- **Tailwind Integration:** Seamless styling with utility-first CSS matching our design tokens
- **Accessibility:** WCAG AA compliance built-in (keyboard navigation, ARIA labels, focus management)
- **Performance:** No runtime overhead, tree-shakeable components
- **TypeScript:** Full type safety for AI-assisted development
- **Rapid Development:** Pre-built patterns for forms, modals, tables, charts (via Recharts integration)

**What Shadcn Provides:**
- **UI Components:** Button, Input, Card, Modal/Dialog, Tabs, Table, Select, Checkbox, Radio, Alert, Badge, Tooltip, Dropdown Menu, Command Palette
- **Form Components:** React Hook Form + Zod validation integration
- **Data Visualization:** Recharts integration for charts
- **Layout:** Container, Grid, Flex utilities via Tailwind
- **State Management:** Works seamlessly with Zustand (our choice)

**Custom Components Needed:**
- Game Board (main inventory visualization)
- Role Selector
- Week Progress Indicator
- Bullwhip Effect Chart (specialized visualization)
- Multi-role Performance Chart
- AI Assessment Question Renderer
- Real-time Player Presence Indicators
- Chat Message Bubble (with AI badge variant)
- Flow Pipes (animated connectors for orders/deliveries)
- Abstract Charts (modern, animated data visualizations)

**Theme Configuration:**
All colors, typography, and spacing tokens defined in Section 3 will be configured in `tailwind.config.js` and Shadcn's theme system for consistent application across all components.

---

## 2. Core User Experience

### 2.1 Defining Experience

The core experience is dual-focused, catering to the distinct needs of students and instructors, while maintaining an overarching feeling of being **excited, in control, curious, determined, and competitive.**

*   **For Students: Effortless Gameplay.** The single most important action is playing the game. The journey from logging in to making a decision each week must be seamless and intuitive. The interface should minimize administrative friction and maximize focus on supply chain strategy, making the learning process feel like engaging gameplay.

*   **For Instructors: Automated Orchestration.** The "magic moment" is the effortless setup and monitoring of a large class session. The platform's value is realized when an instructor can enroll dozens of students, allocate them to games, and monitor their real-time progress from a single dashboard, transforming hours of administrative work into minutes of focused teaching.

### 2.2 Novel UX Patterns

The following novel UX patterns will be implemented to enhance the core experience:

-   **Flow Pipes:** Animated visual connectors will dynamically illustrate the flow of orders and deliveries, providing real-time feedback on game events and increasing engagement.
-   **Live Charts:** Real-time updates to charts will empower players with a sense of control and provide immediate data to inform their strategic decisions.
-   **Team Chat:** The integrated chat feature will foster collaboration and provide a channel for players to seek and offer help, reinforcing the game's core purpose.
-   **AI Player Visual Cues:** When playing with AI opponents, clear visual cues will be provided in the chat (e.g., an AI badge) and through distinct game event notifications to differentiate AI actions from human player interactions.

### 2.3 Core Experience Principles

These principles will guide every UX decision to ensure a consistent and intuitive experience.

*   **Speed & Clarity:** The system will provide immediate and unambiguous feedback when a user's turn is complete. The game will wait for all players to submit their orders before proceeding, ensuring a synchronized and clear turn progression for everyone.
*   **Guidance & Support:** The interface will be designed to be intuitive and self-explanatory. For additional support, users can ask an AI assistant in the chat for help regarding game status or next steps.
*   **Flexibility & Control:** Game configuration is locked for students after the game starts, ensuring a consistent experience. Instructors retain crucial in-game control, such as the ability to substitute inactive players with AI, to ensure the game continues smoothly.
*   **Feedback & Communication:** System feedback will be subtle and informative. Game events and notifications will be delivered through a dedicated, unobtrusive channel, preventing disruption to gameplay while keeping players informed.

---

## 3. Visual Foundation

### 3.1 Color System

**Theme:** Dark Mode ("Mono")

**Palette Structure:**
- **Base:** A dark, monochromatic base for the main UI.
- **Accents:** A unique, vibrant accent color for each of the four roles.

**Complete Palette:**

**Neutrals (Mono Theme):**
- `mono-bg`: #1A1A1A - Main background color
- `mono-surface`: #2C2C2C - Card and surface backgrounds
- `mono-text`: #E0E0E0 - Primary text color
- `mono-light`: #808080 - Secondary text and border color

**Role-Based Accent Colors:**
- `accent-retailer`: #FFD700 (Gold/Amber) - Retailer role
- `accent-wholesaler`: #10B981 (Green) - Wholesaler role
- `accent-distributor`: #8B5CF6 (Purple) - Distributor role
- `accent-factory`: #F97316 (Orange) - Factory role

**Semantic Colors:**
- `success`: #10B981 (Green) - Success states, positive feedback
- `error`: #EF4444 (Red) - Errors, backorders, negative feedback
- `warning`: #F59E0B (Amber) - Warnings and alerts
- `info`: #3B82F6 (Blue) - Informational messages

### 3.2 Typography System

**Font Families:**
- **Game Dashboard & Numeric Data:** `"Roboto Mono", monospace` (for immersive in-game feel, tabular numbers, headings, buttons within the game board)
- **Application UI & Chat:** `"Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif` (for general UI elements, navigation, and chat messages for optimal readability)

**Type Scale (Desktop/Laptop):**
- Base: 16px (1rem), line-height 1.5
- `text-h1`: 40px / 1.2 line-height / -0.02em letter-spacing (Page titles)
- `text-h2`: 32px / 1.25 / -0.015em (Dashboard/panel titles, "Retailer · Week 7 of 20")
- `text-h3`: 24px / 1.3 / -0.015em (Card/component headings)
- `text-h4`: 20px / 1.3 / -0.01em (Subheadings, chart titles)
- `text-body`: 16px / 1.5 / 0 (Body text, chat messages)
- `text-sm`: 14px / 1.4 / 0 (Labels, table headers)
- `text-xs`: 12px / 1.4 / 0 (Captions, helper text, chip labels)

**Mobile/Tablet:** Scale headings down one step (H1 → H2 size)

### 3.3 Spacing System (8pt Grid)

**Tokens:** 4, 8, 12, 16, 24, 32, 40, 48, 64px (all multiples of 4/8)

**Guidelines:**
- Card/panel padding: 16-24px
- Gap between items inside panel: 8-16px
- Gap between major sections: 32px (2× inner spacing)
- Form field gaps: 12-16px

### 3.4 Layout Structure

**Grid System:**
- Desktop (≥1280px): 12-column grid, 24px gutter
- Laptop (1024-1279px): 12-column grid, 16-24px gutter
- Tablet (768-1023px): 8-column grid, 16px gutter

**Game Dashboard Layout:**
- Left sidebar (Dashboard, Analytics, Team, History navigation)
- Main game board (inventory and pipeline visualization)
- Right chat sidebar (team communication)

### 3.5 Accessibility Standards

**Contrast Ratios (WCAG AA Minimum):**
- Normal text: ≥4.5:1 vs background
- Large text (≥18pt or 14pt bold): ≥3:1
- Interactive components: ≥3:1 vs adjacent colors

**Achieved Ratios:**
- Body text (neutral-500 on white): 7.1:1 (AAA)
- Headings (neutral-700 on white): 10.4:1 (AAA)
- Primary buttons (white on primary-500): 4.6:1 (AA)

**Color Independence:**
- Never rely on color alone
- Combine color with icons, labels, and text indicators
- Role colors supplemented with role names in charts

**Interactive Visualizations:**

- Color Theme Explorer: [ux-color-themes.html](./ux-color-themes.html)

---

## 4. Design Direction

### 4.1 Chosen Design Approach

**Selected Design Direction: Immersive Game Board**

This direction, exemplified by `docs/stich/retailer-game-board-beergame.html` (our golden template), prioritizes an engaging and dynamic experience, making the game board the central element. It aligns with the desired student emotions of fun, excitement, and competitiveness.

**Key Characteristics:**
-   **Layout:** Centralized game board with animated flow pipes, flanked by a left sidebar for navigation and a collapsible right sidebar for team chat.
-   **Visual Hierarchy:** The game board is the primary focus, with key performance indicators (KPIs) prominently displayed in the header for quick oversight.
-   **Interaction Patterns:** Animated "Flow Pipes" visually represent orders and deliveries, providing real-time feedback. The chat is interactive and supports AI assistance.
-   **Visual Style:** Dark mode theme with role-specific accent colors used strategically for primary calls-to-action and key highlights.
-   **Typography:** A hybrid approach using `Roboto Mono` for the immersive game dashboard and numeric data, and `Inter` for the application shell and chat for optimal readability.

**Interactive Mockups:**

- **Application Pages Viewer**: [docs/ux-design-directions.html](./ux-design-directions.html)
  - This interactive viewer provides access to all application mockups, starting with the golden template.
- Design Direction Mockups from Stich: [distributor-game-board-beergame.html](./stich/distributor-game-board-beergame.html)
- Design Direction Mockups from Stich: [factory-game-board-beergame.html](./stich/factory-game-board-beergame.html)
- Design Direction Mockups from Stich: [retailer-game-board-beergame.html](./stich/retailer-game-board-beergame.html)
- Design Direction Mockups from Stich: [wholesaler-game-board-beergame.html](./stich/wholesaler-game-board-beergame.html)

---

## 5. User Journey Flows

### 5.1 Critical User Paths

{{user_journey_flows}}

---

## 6. Component Library

### 6.1 Component Strategy

{{component_library_strategy}}

---

## 7. UX Pattern Decisions

### 7.1 Consistency Rules

{{ux_pattern_decisions}}

---

## 8. Responsive Design & Accessibility

### 8.1 Responsive Strategy

{{responsive_accessibility_strategy}}

---

## 9. Implementation Guidance

### 9.1 Completion Summary

{{completion_summary}}

---

## Appendix

### Related Documents

- Product Requirements: `docs/PRD.md`
- Product Brief: `docs/product-brief-beergame-2025-11-13.md`
- Brainstorming: `docs/brainstorming-session-results-2025-10-27.md`

### Core Interactive Deliverables

This UX Design Specification was created through visual collaboration:

- **Color Theme Visualizer**: docs/ux-color-themes.html
  - Interactive HTML showing all color theme options explored
  - Live UI component examples in each theme
  - Side-by-side comparison and semantic color usage

- **Design Direction Mockups**: docs/ux-design-directions.html
  - Interactive HTML with 6-8 complete design approaches
  - Full-screen mockups of key screens
  - Design philosophy and rationale for each direction

### Optional Enhancement Deliverables

_This section will be populated if additional UX artifacts are generated through follow-up workflows._

<!-- Additional deliverables added here by other workflows -->

### Next Steps & Follow-Up Workflows

This UX Design Specification can serve as input to:

- **Wireframe Generation Workflow** - Create detailed wireframes from user flows
- **Figma Design Workflow** - Generate Figma files via MCP integration
- **Interactive Prototype Workflow** - Build clickable HTML prototypes
- **Component Showcase Workflow** - Create interactive component library
- **AI Frontend Prompt Workflow** - Generate prompts for v0, Lovable, Bolt, etc.
- **Solution Architecture Workflow** - Define technical architecture with UX context

### Version History

| Date     | Version | Changes                         | Author        |
| -------- | ------- | ------------------------------- | ------------- |
| 2025-11-13 | 1.0     | Initial UX Design Specification | BIP |
| 2025-11-20 | 1.1     | Standardized typography (Inter for UI, Roboto Mono for Data) | BIP |

---

_This UX Design Specification was created through collaborative design facilitation, not template generation. All decisions were made with user input and are documented with rationale._
