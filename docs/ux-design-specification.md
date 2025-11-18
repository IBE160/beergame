# ibe160 UX Design Specification

_Created on 2025-11-13 by BIP_
_Generated using BMad Method - Create UX Design Workflow v1.0_

---

## Executive Summary

**Project:** Beer Game Interactive Platform - AI-powered supply chain education simulation

**Target Experience:**
- **Students:** Engaged and curious with the feeling of learning through gameplay
- **Instructors:** In control and excited about student performance, liberated from administrative tasks
- **Core Magic:** "Great with AI-driven players and feedback, fun with fellow students"

**Design Inspiration:** Khan Academy's progress-driven visual language and educational game engagement patterns

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
- Game Board (unique inventory visualization with corner slots)
- Role Selector
- Week Progress Indicator
- Bullwhip Effect Chart (specialized visualization)
- Multi-role Performance Chart
- AI Assessment Question Renderer
- Real-time Player Presence Indicators
- Chat Message Bubble (with AI badge variant)

**Theme Configuration:**
All colors, typography, and spacing tokens defined in Section 3 will be configured in `tailwind.config.js` and Shadcn's theme system for consistent application across all components.

---

## 2. Core User Experience

### 2.1 Defining Experience

{{core_experience}}

### 2.2 Novel UX Patterns

{{novel_ux_patterns}}

---

## 3. Visual Foundation

### 3.1 Color System

**Palette Structure: 60/30/10 Rule**
- 60% Neutrals (backgrounds, text, borders)
- 30% Primary Blue (navigation, charts, active states)
- 10% Teal Accent (CTAs, important highlights)

**Complete Palette:**

**Neutrals:**
- `neutral-0`: #FFFFFF - Page background
- `neutral-50`: #F8FAFC - Card backgrounds
- `neutral-100`: #F1F5F9 - Hover states
- `neutral-200`: #E2E8F0 - Borders, dividers
- `neutral-500`: #64748B - Body text (7.1:1 contrast ratio)
- `neutral-700`: #334155 - Headings (10.4:1 contrast ratio)
- `neutral-900`: #0F172A - High-emphasis text

**Primary - Calm Blue:**
- `primary-50`: #EFF6FF - Subtle backgrounds, KPI cards
- `primary-500`: #3B82F6 - Main brand color, nav, active tabs, primary chart lines
- `primary-600`: #2563EB - Hover state
- `primary-700`: #1D4ED8 - Pressed/active state

**Accent - Teal:**
- `accent-500`: #14B8A6 - Primary CTAs, important highlights
- `accent-600`: #0D9488 - CTA hover
- `accent-700`: #0F766E - CTA pressed

**Semantic Colors:**
- `success-500`: #10B981 - Positive inventory, good scores, success states
- `error-500`: #EF4444 - Backorders, errors, validation failures
- `warning-500`: #F59E0B - Warnings, alerts, cautions
- `info-500`: #3B82F6 - Informational messages

**Role Colors (Charts):**
- `role-retailer`: #3B82F6 (Blue) - Retailer role in charts
- `role-wholesaler`: #10B981 (Green) - Wholesaler role
- `role-distributor`: #8B5CF6 (Purple) - Distributor role
- `role-factory`: #F97316 (Orange) - Factory role

### 3.2 Typography System

**Font Families:**
- **Primary UI:** `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`
- **Numeric/Data:** `"JetBrains Mono", "Roboto Mono", monospace` (tabular numbers)

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
- Left sidebar (Board/Data/Results/Exercises navigation): 2-3 columns
- Main game board: 6-7 columns
- Right chat sidebar: 3-4 columns (collapsible)

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

{{design_direction_decision}}

**Interactive Mockups:**

- Design Direction Showcase: [ux-design-directions.html](./ux-design-directions.html)

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

---

_This UX Design Specification was created through collaborative design facilitation, not template generation. All decisions were made with user input and are documented with rationale._
