# AI Frontend Generation Prompt: Beer Game - Game Dashboard

## Project Context

You are building the **Game Dashboard** for the Beer Game Interactive Platform - an AI-powered supply chain education simulation. This is the main screen where students play the game, make ordering decisions, and observe supply chain dynamics in real-time.

## Screen Overview

**Purpose:** Primary gameplay interface where a player (in one of four roles: Retailer, Wholesaler, Distributor, or Factory) makes weekly ordering decisions, views their inventory status, monitors supply chain flow, and communicates with other players.

**User Role:** Student playing as "Retailer" in a multiplayer game
**Game State:** Week 7 of 20-week game, actively playing
**Context:** 4-player multiplayer game (Retailer, Wholesaler, Distributor, Factory)

## Technical Stack

- **Framework:** Next.js 14+ with TypeScript
- **Styling:** Tailwind CSS
- **UI Components:** Shadcn UI (use shadcn components where applicable)
- **State Management:** Zustand or React Context
- **Charts:** Recharts
- **Fonts:** System fonts (no external font loading)

## Design System Specifications

### Color Palette

```css
/* Neutrals */
--neutral-0: #FFFFFF;
--neutral-50: #F8FAFC;
--neutral-100: #F1F5F9;
--neutral-200: #E2E8F0;
--neutral-500: #64748B;
--neutral-700: #334155;
--neutral-900: #0F172A;

/* Primary - Calm Blue */
--primary-50: #EFF6FF;
--primary-500: #3B82F6;
--primary-600: #2563EB;
--primary-700: #1D4ED8;

/* Accent - Teal */
--accent-500: #14B8A6;
--accent-600: #0D9488;
--accent-700: #0F766E;

/* Semantic */
--success-500: #10B981;
--error-500: #EF4444;
--warning-500: #F59E0B;
--info-500: #3B82F6;

/* Role Colors */
--role-retailer: #3B82F6;
--role-wholesaler: #10B981;
--role-distributor: #8B5CF6;
--role-factory: #F97316;
```

### Typography

```css
/* Font Families */
font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
font-family-mono: "JetBrains Mono", "Roboto Mono", monospace;

/* Type Scale */
--text-h1: 40px / 1.2 / -0.02em letter-spacing;
--text-h2: 32px / 1.25 / -0.015em;
--text-h3: 24px / 1.3 / -0.015em;
--text-h4: 20px / 1.3 / -0.01em;
--text-body: 16px / 1.5 / 0;
--text-sm: 14px / 1.4 / 0;
--text-xs: 12px / 1.4 / 0;
```

### Spacing (8pt Grid)

Use multiples of 4/8px: `4, 8, 12, 16, 24, 32, 40, 48, 64`

- Card/panel padding: 16-24px
- Gap between items inside panel: 8-16px
- Gap between major sections: 32px

## Layout Structure

**Grid Layout:** 3-column dashboard

```
┌─────────────────────────────────────────────────────────────┐
│ Left Sidebar │      Main Content Area        │ Right Chat   │
│   (200px)    │         (flexible)            │   (300px)    │
│              │                                │              │
│  Navigation  │  Header (blue bar with KPIs)  │              │
│  - Board     │  ─────────────────────────────│  Chat Header │
│  - Data      │                                │              │
│  - Results   │  Game Board (3x3 grid)        │  Messages    │
│  - Exercises │  ├─ Incoming Order             │  - AI msgs   │
│              │  ├─ Inventory (center)        │  - Player    │
│              │  └─ Outgoing Order            │              │
│              │                                │              │
│              │  Charts Section               │              │
│              │  - Order & Inventory Trend    │  Chat Input  │
│              │                                │              │
│              │  Action Bar (bottom)          │              │
└─────────────────────────────────────────────────────────────┘
```

**Responsive:** Desktop/Laptop minimum 1024px width (tablet/desktop only, no mobile)

## Component Specifications

### 1. Top Header Bar

**Background:** `--primary-500` (#3B82F6)
**Color:** White
**Padding:** 16px 24px
**Layout:** Flex, space-between

**Left Section:**
- **Title:** "Retailer · Week 7 of 20" (text-h2, 32px, white, bold)
- **Subtitle:** "Multiplayer Game with 3 players" (text-sm, 14px, white, opacity 90%)

**Right Section - KPI Bar:**
Three KPI metrics displayed horizontally with 24px gap:

**KPI Structure (each):**
- Label: 12px, uppercase, letter-spacing 0.05em, opacity 80%
- Value: 24px, bold, monospace font

**KPIs:**
1. **Total Cost:** $2,450 (white)
2. **Inventory:** +12 (color: --success-500 #10B981)
3. **Backlog:** -5 (color: --error-500 #EF4444)

### 2. Left Sidebar Navigation

**Width:** 200px
**Background:** `--neutral-50` (#F8FAFC)
**Border-right:** 1px solid `--neutral-200`
**Padding:** 16px

**Navigation Items:**
- Board (active)
- Data & Charts
- Results
- Exercises

**Nav Item Style:**
- Default: padding 12px 16px, border-radius 8px, color `--neutral-500`
- Hover: background `--neutral-200`
- Active: background `--primary-500`, color white

### 3. Game Board (Central Component)

**Container:**
- Background: white
- Border: 2px solid `--primary-500`
- Border-radius: 12px
- Padding: 24px
- Margin-bottom: 24px

**Grid:** 3x3 grid with 16px gap

**Grid Slots (9 total):**

**Slot Structure:**
```
├─ Border: 2px solid --neutral-200
├─ Border-radius: 8px
├─ Padding: 16px
├─ Text-align: center
└─ Components:
   ├─ Label: 12px, --neutral-500, uppercase, margin-bottom 8px
   └─ Value: 32px, bold, monospace, --primary-500
```

**Grid Layout:**
```
Row 1: [Incoming Order: 8] [Incoming Delivery: 12] [Customer Demand: 10]
Row 2: [Pipeline In: 15]    [INVENTORY: +12]       [Pipeline Out: 8]
Row 3: [Last Week Order: 15] [Outgoing Delivery: 10] [Backlog: -5]
```

**Center Slot (Inventory) - Highlighted:**
- Border-color: `--primary-500` (2px)
- Background: `--primary-50` (#EFF6FF)
- Value color:
  - Positive inventory: `--success-500` (green)
  - Negative (backlog): `--error-500` (red)

**Slot Labels:**
- Incoming Order
- Incoming Delivery
- Customer Demand
- Pipeline In
- Inventory (center, highlighted)
- Pipeline Out
- Last Week Order
- Outgoing Delivery
- Backlog

**Slot Values (sample data):**
- Incoming Order: 8
- Incoming Delivery: 12
- Customer Demand: 10
- Pipeline In: 15
- Inventory: +12 (green)
- Pipeline Out: 8
- Last Week Order: 15
- Outgoing Delivery: 10
- Backlog: -5 (red)

### 4. Charts Section

**Container:**
- Background: `--neutral-50`
- Border: 1px solid `--neutral-200`
- Border-radius: 8px
- Padding: 16px
- Margin-bottom: 16px

**Title:** "Order & Inventory Trend" (text-h4, 20px, `--neutral-700`)

**Chart (use Recharts):**
- Type: Line chart
- Height: 180px
- X-axis: Weeks 1-7
- Y-axis: Units (0-30 range)
- Two lines:
  - Orders: `--primary-500` (blue), 2px stroke
  - Inventory: `--success-500` (green), 2px stroke
- Grid: subtle dotted lines
- Tooltip: Show week, order value, inventory value

**Sample Data:**
```javascript
const chartData = [
  { week: 1, orders: 8, inventory: 12 },
  { week: 2, orders: 10, inventory: 10 },
  { week: 3, orders: 12, inventory: 8 },
  { week: 4, orders: 15, inventory: 5 },
  { week: 5, orders: 12, inventory: 8 },
  { week: 6, orders: 15, inventory: 12 },
  { week: 7, orders: 8, inventory: 12 }
];
```

### 5. Right Chat Sidebar

**Width:** 300px
**Background:** `--neutral-50`
**Border-left:** 1px solid `--neutral-200`
**Padding:** 16px
**Layout:** Flex column

**Chat Header:**
- Text: "Team Chat"
- Font-size: 16px, font-weight 600, color `--neutral-700`
- Margin-bottom: 16px
- Border-bottom: 1px solid `--neutral-200`, padding-bottom 12px

**Messages Container:**
- Flex: 1
- Overflow-y: auto
- Max-height: calc(100% - 100px)

**Message Bubble:**
- Background: `--neutral-200` (#E2E8F0)
- Padding: 8px 12px
- Border-radius: 8px
- Margin-bottom: 8px
- Font-size: 14px

**AI Message Variant:**
- Background: `--primary-50` (#DBEAFE)
- Border-left: 3px solid `--primary-500`

**Sample Messages:**
```
[AI] Week 7 started. Customer demand: 10 units.
[Wholesaler] I have enough stock
[You] Ordering 15 units
```

**Message Format:**
- AI messages: "[AI]: {message}"
- Player messages: "[Role]: {message}"
- User messages: "You: {message}"

**Chat Input (bottom):**
- Input field: full width, padding 8px 12px
- Border: 1px solid `--neutral-200`
- Border-radius: 6px
- Placeholder: "Type a message..."

### 6. Bottom Action Bar

**Background:** `--neutral-50`
**Border-top:** 1px solid `--neutral-200`
**Padding:** 16px 24px
**Layout:** Flex, space-between, align-center

**Left Section - Input Group:**
- Label: "Order Quantity:" (14px, `--neutral-500`, margin-right 12px)
- Input:
  - Width: 100px
  - Padding: 8px 12px
  - Border: 1px solid `--neutral-200`
  - Border-radius: 6px
  - Font-size: 16px
  - Font-family: monospace
  - Value: 15
  - Type: number

**Right Section - Submit Button:**
- Text: "Submit Order"
- Background: `--accent-500` (#14B8A6, teal)
- Color: white
- Padding: 10px 20px
- Border-radius: 6px
- Font-size: 14px, font-weight 600
- Hover: background `--accent-600` (#0D9488)
- Cursor: pointer

## Interactive Behaviors

### Hover States
- Navigation items: Background to `--neutral-200`
- Submit button: Background to `--accent-600`
- Board slots: Subtle scale(1.02) or shadow increase

### Focus States
- Input fields: Border `--primary-500`, box-shadow 0 0 0 3px `--primary-50`
- All interactive elements: Visible focus ring

### Active States
- Active nav item: Background `--primary-500`, color white
- Pressed button: Background `--accent-700`

### Animations
- All transitions: 200ms ease
- Hover/focus: smooth color/background transitions
- No complex animations (keep it performant)

## Accessibility Requirements

- All interactive elements: keyboard navigable (Tab)
- ARIA labels on all inputs and buttons
- Color contrast: All text meets WCAG AA (4.5:1 minimum)
- Focus indicators: Visible on all interactive elements
- Input labels: Properly associated with `<label>` and `for` attributes

## Data/State Structure

```typescript
interface GameState {
  role: 'Retailer' | 'Wholesaler' | 'Distributor' | 'Factory';
  currentWeek: number;
  totalWeeks: number;
  totalCost: number;
  inventory: number;
  backlog: number;
  incomingOrder: number;
  incomingDelivery: number;
  customerDemand: number;
  pipelineIn: number;
  pipelineOut: number;
  lastWeekOrder: number;
  outgoingDelivery: number;
  orderQuantity: number;
  chartData: { week: number; orders: number; inventory: number }[];
  messages: { sender: string; message: string; isAI: boolean }[];
}

// Sample initial state
const initialState: GameState = {
  role: 'Retailer',
  currentWeek: 7,
  totalWeeks: 20,
  totalCost: 2450,
  inventory: 12,
  backlog: -5,
  incomingOrder: 8,
  incomingDelivery: 12,
  customerDemand: 10,
  pipelineIn: 15,
  pipelineOut: 8,
  lastWeekOrder: 15,
  outgoingDelivery: 10,
  orderQuantity: 15,
  chartData: [
    { week: 1, orders: 8, inventory: 12 },
    { week: 2, orders: 10, inventory: 10 },
    { week: 3, orders: 12, inventory: 8 },
    { week: 4, orders: 15, inventory: 5 },
    { week: 5, orders: 12, inventory: 8 },
    { week: 6, orders: 15, inventory: 12 },
    { week: 7, orders: 8, inventory: 12 }
  ],
  messages: [
    { sender: 'AI', message: 'Week 7 started. Customer demand: 10 units.', isAI: true },
    { sender: 'Wholesaler', message: 'I have enough stock', isAI: false },
    { sender: 'You', message: 'Ordering 15 units', isAI: false }
  ]
};
```

## Functional Requirements

1. **Display current game state** - Show all board values dynamically from state
2. **Order input** - Allow user to type order quantity (number input, 0-100 range)
3. **Submit order** - Button click handler (console.log for now)
4. **Navigation** - Switch between views (Board is active by default)
5. **Chart rendering** - Display line chart with sample data using Recharts
6. **Chat display** - Show messages with AI vs player styling
7. **Responsive layout** - Maintain 3-column structure on desktop (1024px+)

## Implementation Notes

- Use Shadcn UI components for Button, Input, Card where applicable
- Implement layout with Tailwind CSS Grid
- Chart: Use `<LineChart>` from Recharts with responsive container
- State: Use React hooks (useState) or Zustand store
- TypeScript: Fully typed components and props
- No external API calls needed (use mock data)
- Component should be self-contained and fully functional

## Success Criteria

- ✓ Layout matches 3-column structure exactly
- ✓ All colors from design system applied correctly
- ✓ Typography scale matches specification (H2: 32px, body: 16px, etc.)
- ✓ 8pt spacing grid followed throughout
- ✓ Game board displays all 9 slots in 3x3 grid
- ✓ Center inventory slot is highlighted with blue border and light blue background
- ✓ KPIs in header show correct colors (green for positive, red for negative)
- ✓ Chart renders with two lines (orders, inventory)
- ✓ Chat messages display with AI badge/styling
- ✓ Submit button uses teal accent color
- ✓ All hover/focus states work
- ✓ Fully keyboard accessible
- ✓ Responsive (works at 1024px+ width)

## Design Philosophy

This dashboard balances **calm professionalism** (educational context) with **engaged curiosity** (game experience). The calm blue primary color creates focus and trust, while teal accents add excitement to key actions. The layout prioritizes the game board (center of attention) while keeping KPIs visible and chat accessible for multiplayer coordination.

---

**Generate a fully functional, production-ready React component matching this specification exactly.**
