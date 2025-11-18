# AI Frontend Generation Prompt: Beer Game - Game Dashboard (Retailer Role)

## Project Context

You are building the **Game Dashboard** for the Beer Game Interactive Platform - an AI-powered supply chain education simulation. This is the main screen where students play the game, make ordering decisions, and observe supply chain dynamics in real-time.

This dashboard replicates the original physical MIT Beer Game board layout, showing inventory facilities, transportation pipelines, and the flow of goods and orders through the supply chain.

## Screen Overview

**Purpose:** Primary gameplay interface where a player views their supply chain position, makes weekly ordering decisions, monitors inventory flow, views real-time charts, and communicates with other players.

**User Role:** Student playing as **Retailer** in a multiplayer game
**Game State:** Week 7 of 20-week game, actively playing
**Context:** 4-player multiplayer game (Retailer, Wholesaler, Distributor, Factory)

## Reference Images

See `docs/references/images/retailer-large.png` for the exact layout structure.

**Key Visual Concepts:**
- Central inventory facility (rectangular, like a warehouse seen from above)
- Corner slots inside inventory showing: Incoming Order (SW), Outgoing Order (NW), Incoming Delivery (NE), Outgoing Delivery (SE)
- Pipeline slots showing Week 1 and Week 2 for transportation lead times
- Thick green arrows showing flow: goods flow top-down, orders flow bottom-up
- Two chart areas embedded within the board component
- Role label ("Retailer") centered at bottom

## Technical Stack

- **Framework:** Next.js 14+ with TypeScript
- **Styling:** Tailwind CSS
- **UI Components:** Shadcn UI
- **State Management:** Zustand or React Context
- **Charts:** Recharts (LineChart, AreaChart)
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

/* Semantic */
--success-500: #10B981; /* Positive inventory, green arrows/pipelines */
--error-500: #EF4444;   /* Negative inventory (backorders) */
--warning-500: #F59E0B;
--info-500: #3B82F6;

/* Role Color */
--role-retailer: #3B82F6; /* Blue for Retailer */
```

### Typography

```css
/* Font Families */
font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
font-family-mono: "JetBrains Mono", "Roboto Mono", monospace;

/* Type Scale */
--text-h1: 40px / 1.2 / -0.02em;
--text-h2: 32px / 1.25 / -0.015em;
--text-h3: 24px / 1.3 / -0.015em;
--text-h4: 20px / 1.3 / -0.01em;
--text-body: 16px / 1.5 / 0;
--text-sm: 14px / 1.4 / 0;
--text-xs: 12px / 1.4 / 0;
```

### Spacing (8pt Grid)

Use multiples of 4/8px: `4, 8, 12, 16, 24, 32, 40, 48, 64`

## Overall Layout Structure

**3-Column Dashboard Layout:**

```
┌──────────────────────────────────────────────────────────────────┐
│ [L Sidebar]    [Main Content - Game Board + Charts]  [R Chat]   │
│  200px         flexible width                         300px      │
│                                                                   │
│ ┌─────────┐   ┌─────────────────────────────────┐   ┌────────┐ │
│ │         │   │ Header Bar (blue, KPIs)         │   │ Chat   │ │
│ │ Nav     │   ├─────────────────────────────────┤   │ Header │ │
│ │ - Board │   │                                  │   │────────│ │
│ │ - Data  │   │  Game Board Component            │   │        │ │
│ │ - Result│   │  (Inventory facility + pipelines)│   │Messages│ │
│ │ - Exerc │   │                                  │   │        │ │
│ │         │   │  ┌──────────────────────────┐   │   │        │ │
│ │         │   │  │ Inventory Facility       │   │   │        │ │
│ │         │   │  │  w/ corner slots         │   │   │        │ │
│ │         │   │  │  + pipelines             │   │   │        │ │
│ │         │   │  └──────────────────────────┘   │   │        │ │
│ │         │   │                                  │   │        │ │
│ │         │   │  [Chart 1]     [Chart 2]        │   │        │ │
│ │         │   │                                  │   │        │ │
│ └─────────┘   └─────────────────────────────────┘   └────────┘ │
│               ┌──────────────────────────────────┐              │
│               │ Bottom Action Bar                │              │
│               │ (Order input + Submit button)    │              │
│               └──────────────────────────────────┘              │
└──────────────────────────────────────────────────────────────────┘
```

**Responsive:** Desktop/Laptop minimum 1024px width (no mobile in MVP)

## Component Specifications

### 1. Top Header Bar (Blue KPI Bar)

**Full-width, spans all three columns**

**Background:** `--primary-500` (#3B82F6)
**Color:** White
**Padding:** 16px 24px
**Layout:** Flex, space-between

**Left Section:**
- **Title:** "Retailer · Week 7 of 20" (text-h3, 24px, white, bold)
- **Subtitle:** "Multiplayer Game" (text-sm, 14px, white, opacity 90%)

**Right Section - KPI Bar:**
Three KPI metrics horizontal with 24px gap:

**KPI Structure:**
- Label: 12px, uppercase, letter-spacing 0.05em, opacity 80%
- Value: 24px, bold, monospace

**KPIs:**
1. **Total Cost:** $2,450 (white)
2. **Inventory:** +12 (color: `--success-500` green if positive, `--error-500` red if negative)
3. **Backlog:** 0 or negative value (color: `--error-500` red if > 0)

### 2. Left Sidebar Navigation

**Width:** 200px
**Background:** `--neutral-50` (#F8FAFC)
**Border-right:** 1px solid `--neutral-200`
**Padding:** 16px
**Grid-row:** Spans from header to bottom

**Navigation Items (vertical list):**
- **Board** (active - highlighted)
- **Data & Charts**
- **Results**
- **Exercises**

**Nav Item Style:**
- Default: padding 12px 16px, border-radius 8px, color `--neutral-500`, font-size 14px
- Hover: background `--neutral-200`
- Active: background `--primary-500`, color white, font-weight 600

**Collapsible Behavior (Optional Enhancement):**
- Can collapse to show only icons
- Expand on hover or click

### 3. Main Game Board Component (Center Column)

This is the CORE component - the inventory facility with pipelines.

**Container:**
- Background: `--neutral-0` (white)
- Padding: 24px
- Overflow-y: auto

#### 3A. Inventory Facility Structure

**Visual Concept:** Large rectangular facility (like warehouse seen from above) with corner slots and center inventory display.

**Main Inventory Rectangle:**
- Width: 600px (or flexible, but maintain aspect ratio)
- Height: 400px
- Border: 3px solid `--neutral-200`
- Border-radius: 12px
- Background: white
- Position: Relative (for absolute positioning of corner slots)
- Box-shadow: subtle

**Corner Slots (4 slots positioned absolutely in corners):**

Each corner slot:
- Width: 140px
- Height: 80px
- Border: 2px solid `--neutral-300`
- Border-radius: 8px
- Background: `--neutral-50`
- Padding: 12px
- Text-align: center

**Corner Slot Positions & Labels:**

1. **North-West (top-left):**
   - Position: top: 20px, left: 20px
   - Label: "Outgoing Order" (text-xs, 12px, `--neutral-500`, underline)
   - Value: 15 (text-h4, 20px, monospace, `--primary-500`)
   - **Decision Point:** This is the ONLY editable value (input field when it's the player's turn)

2. **North-East (top-right):**
   - Position: top: 20px, right: 20px
   - Label: "Incoming Delivery" (text-xs, 12px, `--neutral-500`)
   - Value: 12 (text-h4, 20px, monospace, `--neutral-700`)

3. **South-West (bottom-left):**
   - Position: bottom: 20px, left: 20px
   - Label: "Incoming Order" (text-xs, 12px, `--neutral-500`, underline)
   - Value: 8 (text-h4, 20px, monospace, `--neutral-700`)

4. **South-East (bottom-right):**
   - Position: bottom: 20px, right: 20px
   - Label: "Outgoing Delivery" (text-xs, 12px, `--neutral-500`)
   - Value: 10 (text-h4, 20px, monospace, `--neutral-700`)

**Center Inventory Display:**
- Position: Absolute center of rectangle
- Width: 160px
- Height: 100px
- Border: 3px solid `--primary-500` (blue, prominent)
- Border-radius: 8px
- Background: `--primary-50` (light blue tint)
- Text-align: center
- Padding: 16px

**Center Content:**
- Label: "Inventory" (text-sm, 14px, `--neutral-700`, margin-bottom 8px)
- Value: +12 (text-h2, 32px, bold, monospace)
  - Green (`--success-500`) if positive
  - Red (`--error-500`) if negative (represents backorders)

#### 3B. Pipeline/Transportation Slots (Retailer-specific)

**Incoming Delivery Pipeline (Above inventory facility):**

Two rectangular slots stacked vertically, connected by arrow, positioned ABOVE the inventory facility.

**Pipeline Container:**
- Position: Above inventory rectangle (margin-top: -60px from container top)
- Align: Right side (matching Incoming Delivery corner slot)

**Week Slots:**
- Each slot: 100px × 60px
- Border: 2px solid `--neutral-300`
- Border-radius: 6px
- Background: `--neutral-100`
- Text-align: center
- Padding: 8px

**Slot 1 (Top):**
- Label: "Week 2" (text-xs, `--neutral-500`)
- Value: 10 (text-body, 16px, monospace, `--neutral-700`)

**Slot 2 (Middle):**
- Label: "Week 1" (text-xs, `--neutral-500`)
- Value: 25 (text-body, 16px, monospace, `--neutral-700`)

**Arrow between Week slots:**
- Thick arrow (8px wide, `--success-500` green)
- Points downward (Week 2 → Week 1)
- SVG or CSS triangle

**Arrow from Week 1 to Incoming Delivery:**
- Thick arrow (8px wide, `--success-500` green)
- Points from Week 1 slot to Incoming Delivery corner slot
- SVG path or CSS

**Arrow from Incoming Order to Inventory:**
- Thick arrow pointing from Incoming Order corner (SW) toward center Inventory
- Color: `--success-500` (green)
- Width: 8px
- Full height spanning from Incoming Order slot to inventory edge

**Outgoing Delivery Pipeline (Below inventory facility):**

Positioned BELOW the inventory facility, no Week slots for Retailer (simplified).

**Arrow from Outgoing Delivery to Customer:**
- Thick arrow (8px wide, `--success-500` green)
- Points downward OUT of the board
- Label near arrow: "To Customer" (text-xs, `--neutral-500`)

**Arrow from Inventory to Outgoing Delivery:**
- Thick arrow pointing from center Inventory to Outgoing Delivery corner (SE)
- Color: `--success-500` green
- Width: 8px

**Incoming Demand Arrow (pointing into Incoming Order):**
- Thick arrow (8px wide, `--info-500` blue)
- Points upward INTO Incoming Order slot from below
- Label: "Customer Demand" (text-xs, `--neutral-500`)
- Full height matching the other arrows

#### 3C. Role Label at Bottom

Below the entire inventory facility + pipelines:

- Text: "Retailer" (text-h3, 24px, centered, `--neutral-700`, font-weight 600)
- Margin-top: 24px

#### 3D. Embedded Charts (Below game board, inside main column)

**Two charts side-by-side in a grid:**

**Container:**
- Display: grid
- Grid-template-columns: 1fr 1fr
- Gap: 24px
- Margin-top: 32px

**Chart 1: Order & Inventory Trend (Multi-line)**

**Container:**
- Background: `--neutral-50`
- Border: 1px solid `--neutral-200`
- Border-radius: 8px
- Padding: 16px

**Title:** "Orders & Inventory" (text-h4, 20px, `--neutral-700`, margin-bottom 12px)

**Chart (Recharts LineChart):**
- Height: 200px
- Responsive container
- X-axis: Weeks 1-7
- Y-axis: Quantity (0-30)
- Two lines:
  1. **Outgoing Orders** (player decisions): `--primary-500` blue, 2px stroke, as BAR series
  2. **Inventory Level**: `--success-500` green, 2px stroke, line series
- Grid: subtle dotted lines (`--neutral-200`)
- Legend: bottom
- Tooltip: Show week, values

**Sample Data:**
```javascript
[
  { week: 1, orders: 8, inventory: 12 },
  { week: 2, orders: 10, inventory: 10 },
  { week: 3, orders: 12, inventory: 8 },
  { week: 4, orders: 15, inventory: 5 },
  { week: 5, orders: 12, inventory: 8 },
  { week: 6, orders: 15, inventory: 12 },
  { week: 7, orders: 8, inventory: 12 }
]
```

**Chart 2: Cost Accumulation (Stacked Area)**

**Container:** (same styling as Chart 1)

**Title:** "Cost Breakdown" (text-h4, 20px, `--neutral-700`)

**Chart (Recharts AreaChart):**
- Height: 200px
- X-axis: Weeks 1-7
- Y-axis: Cost ($)
- Stacked areas:
  1. **Inventory Holding Cost**: `--success-500` green at 40% opacity
  2. **Backorder Cost**: `--error-500` red at 40% opacity
- Grid: subtle
- Legend: bottom
- Tooltip: Show total cost on hover

**Sample Data:**
```javascript
[
  { week: 1, holding: 120, backorder: 0 },
  { week: 2, holding: 100, backorder: 50 },
  { week: 3, holding: 80, backorder: 100 },
  { week: 4, holding: 50, backorder: 150 },
  { week: 5, holding: 80, backorder: 100 },
  { week: 6, holding: 120, backorder: 50 },
  { week: 7, holding: 120, backorder: 0 }
]
```

### 4. Right Chat Sidebar

**Width:** 300px
**Background:** `--neutral-50`
**Border-left:** 1px solid `--neutral-200`
**Padding:** 16px
**Layout:** Flex column
**Grid-row:** Spans from header to bottom

**Chat Header:**
- Text: "Team Chat" (text-h4, 16px, font-weight 600, `--neutral-700`)
- Margin-bottom: 16px
- Border-bottom: 1px solid `--neutral-200`, padding-bottom 12px

**Channel Selector (Optional):**
- Dropdown or tabs showing:
  - Game Channel (all players)
  - Role Channel (not applicable for single role)
  - Instructor Channel
- Font-size: 14px

**Messages Container:**
- Flex: 1
- Overflow-y: auto
- Max-height: calc(100vh - 300px)

**Message Bubble:**
- Background: `--neutral-200` (#E2E8F0)
- Padding: 10px 12px
- Border-radius: 8px
- Margin-bottom: 8px
- Font-size: 14px
- Line-height: 1.4

**AI Message Variant:**
- Background: `--primary-50` (#DBEAFE)
- Border-left: 3px solid `--primary-500`
- Font-style: italic (optional)
- Prefix: "AI: " or icon

**Sample Messages:**
```
[AI] Week 7 started. Customer demand: 10 units.
[Wholesaler] I have enough stock
[You] Ordering 15 units this week
```

**Chat Input (Bottom):**
- Position: Sticky bottom
- Input field: full width, padding 10px 12px
- Border: 1px solid `--neutral-200`
- Border-radius: 6px
- Placeholder: "Type message..."
- Font-size: 14px

### 5. Bottom Action Bar

**Full-width, spans main content column only (not sidebars)**

**Background:** `--neutral-100`
**Border-top:** 1px solid `--neutral-200`
**Padding:** 16px 24px
**Layout:** Flex, space-between, align-center
**Position:** Sticky bottom

**Left Section - Current Week Indicator:**
- Text: "Week 7 of 20" (text-body, 16px, `--neutral-700`, font-weight 600)
- Optional: Progress bar showing 7/20

**Center Section - Order Input:**

**Label:** "Your Order for Week 8:" (text-sm, 14px, `--neutral-700`, margin-right 12px)

**Input:**
- Type: number
- Width: 120px
- Padding: 10px 14px
- Border: 2px solid `--neutral-300`
- Border-radius: 6px
- Font-size: 18px
- Font-family: monospace
- Value: 15
- Min: 0, Max: 100
- Focus: border-color `--primary-500`, box-shadow

**Right Section - Submit Button:**
- Text: "Submit Order"
- Background: `--accent-500` (#14B8A6, teal)
- Color: white
- Padding: 12px 24px
- Border-radius: 6px
- Font-size: 16px
- Font-weight: 600
- Hover: background `--accent-600`
- Cursor: pointer
- Disabled state: opacity 50%, cursor not-allowed

**Waiting State (after submit):**
- Show "Waiting for other players..." message
- Disable submit button
- Optional: Loading spinner

## Interactive Behaviors

### Hover States
- Navigation items: Background to `--neutral-200`
- Submit button: Background to `--accent-600`
- Corner slots: Subtle scale(1.02) or shadow increase
- Chart lines: Highlight on hover

### Focus States
- Input fields: Border `--primary-500`, box-shadow 0 0 0 3px `--primary-50`
- All interactive elements: Visible focus ring (2px `--primary-500`)

### Active/Playing States
- Active nav item: Background `--primary-500`, color white
- Current player's turn: Green glow on "Outgoing Order" slot
- Waiting for others: Subtle pulse animation on waiting message

### Animation States (Future Enhancement)
- Week transition: Arrows animate showing flow
- Inventory update: Number change with smooth transition
- Pipeline movement: Week 2 → Week 1 → Delivery (as described in proposal)

## Accessibility Requirements

- **Keyboard Navigation:** All interactive elements Tab-accessible
- **ARIA Labels:**
  - Game board: `aria-label="Game board showing inventory and pipeline status"`
  - Inventory: `aria-live="polite"` for real-time updates
  - Charts: Proper labels and descriptions
- **Color Contrast:**
  - All text meets WCAG AA (4.5:1 minimum)
  - Green arrows: ensure sufficient contrast
- **Focus Indicators:** Visible 2px ring on all interactive elements
- **Screen Reader:** Announce week changes, inventory updates
- **Alt Text:** Describe arrow flows and pipeline states

## Data/State Structure

```typescript
interface GameBoardState {
  // Player info
  role: 'Retailer' | 'Wholesaler' | 'Distributor' | 'Factory';
  currentWeek: number;
  totalWeeks: number;

  // KPIs
  totalCost: number;
  inventoryLevel: number; // positive or negative
  backlog: number;

  // Corner slots
  incomingOrder: number;     // SW corner
  outgoingOrder: number;     // NW corner (editable)
  incomingDelivery: number;  // NE corner
  outgoingDelivery: number;  // SE corner

  // Pipeline (Retailer)
  incomingPipeline: {
    week1: number;
    week2: number;
  };

  // Customer demand (for Retailer)
  customerDemand: number;

  // Chart data
  orderHistory: { week: number; orders: number; inventory: number }[];
  costHistory: { week: number; holding: number; backorder: number }[];

  // Chat
  messages: { sender: string; message: string; isAI: boolean; timestamp: Date }[];

  // Game state
  isPlayerTurn: boolean;
  waitingForPlayers: boolean;
  gameStatus: 'playing' | 'waiting' | 'completed';
}

// Sample initial state
const initialState: GameBoardState = {
  role: 'Retailer',
  currentWeek: 7,
  totalWeeks: 20,
  totalCost: 2450,
  inventoryLevel: 12,
  backlog: 0,
  incomingOrder: 8,
  outgoingOrder: 15,
  incomingDelivery: 12,
  outgoingDelivery: 10,
  incomingPipeline: { week1: 25, week2: 10 },
  customerDemand: 10,
  orderHistory: [
    { week: 1, orders: 8, inventory: 12 },
    { week: 2, orders: 10, inventory: 10 },
    { week: 3, orders: 12, inventory: 8 },
    { week: 4, orders: 15, inventory: 5 },
    { week: 5, orders: 12, inventory: 8 },
    { week: 6, orders: 15, inventory: 12 },
    { week: 7, orders: 8, inventory: 12 }
  ],
  costHistory: [
    { week: 1, holding: 120, backorder: 0 },
    { week: 2, holding: 100, backorder: 50 },
    { week: 3, holding: 80, backorder: 100 },
    { week: 4, holding: 50, backorder: 150 },
    { week: 5, holding: 80, backorder: 100 },
    { week: 6, holding: 120, backorder: 50 },
    { week: 7, holding: 120, backorder: 0 }
  ],
  messages: [
    { sender: 'AI', message: 'Week 7 started. Customer demand: 10 units.', isAI: true, timestamp: new Date() },
    { sender: 'Wholesaler', message: 'I have enough stock', isAI: false, timestamp: new Date() },
    { sender: 'You', message: 'Ordering 15 units', isAI: false, timestamp: new Date() }
  ],
  isPlayerTurn: true,
  waitingForPlayers: false,
  gameStatus: 'playing'
};
```

## Functional Requirements

1. **Display game board** - Render inventory facility with corner slots, center inventory, and pipelines
2. **Show arrows** - Render thick green arrows showing flow (SVG or CSS)
3. **Display pipeline values** - Show Week 1, Week 2 transportation slots
4. **Order input** - Number input in "Outgoing Order" corner slot when player's turn
5. **Submit order** - Button click handler (console.log order, set waiting state)
6. **Navigation** - Switch between Board/Data/Results/Exercises views
7. **Chart rendering** - Two Recharts (LineChart + AreaChart) with live data
8. **Chat display** - Scrollable messages with AI styling
9. **Responsive layout** - Maintain 3-column structure on desktop (1024px+)
10. **Real-time updates** - Inventory, costs, charts update dynamically

## Implementation Notes

- **Layout:** Use CSS Grid for 3-column structure
- **Game Board:** Relative positioning for inventory facility, absolute positioning for corner slots
- **Arrows:** SVG paths or CSS pseudo-elements (`::before`/`::after`) with triangular borders
- **Charts:** Recharts `<ResponsiveContainer>`, `<LineChart>`, `<AreaChart>`
- **State:** React hooks (useState) or Zustand store
- **TypeScript:** Fully typed components
- **Shadcn:** Use Button, Input, Card, Tabs components where applicable
- **No API calls:** Use mock data for standalone demo

## Visual Design Philosophy

**Flow Visualization:**
- **Goods flow:** Top-down (deliveries come from above, go to customer below)
- **Order flow:** Bottom-up (orders come from customer, go upstream)
- **Green arrows:** Represent physical flow of goods/beer
- **Blue arrows:** Represent information/order flow
- **Underlined labels:** Indicate decision points or inputs

**Hierarchy:**
- **Center Inventory:** Most prominent (thick blue border, light blue background)
- **Corner Slots:** Secondary importance (neutral colors)
- **Pipelines:** Tertiary (showing delay/lead time)
- **Charts:** Support decision-making (embedded below board)

## Success Criteria

- ✓ Layout matches 3-column structure (sidebar, main, chat)
- ✓ Inventory facility rendered with 4 corner slots correctly positioned
- ✓ Center inventory prominently displayed with color coding (green/red)
- ✓ Pipeline slots show Week 1 and Week 2 above inventory
- ✓ Thick green arrows rendered showing flow direction
- ✓ All corner slot labels and values displayed correctly
- ✓ Two charts embedded below game board (Orders+Inventory, Cost)
- ✓ Charts render with correct data using Recharts
- ✓ Chat sidebar displays messages with AI styling
- ✓ Order input functional in Outgoing Order slot
- ✓ Submit button uses teal accent color
- ✓ KPIs in header show correct colors (green positive, red negative)
- ✓ All typography follows scale (H2: 32px, H3: 24px, H4: 20px, body: 16px)
- ✓ 8pt spacing grid followed throughout
- ✓ All colors from design system applied
- ✓ Hover/focus states work correctly
- ✓ Fully keyboard accessible
- ✓ Responsive at 1024px+ width

## Future Enhancements (Not in MVP)

- Animation: Week transitions with moving arrows
- Collapsible sidebars: Left nav and right chat
- Multiple chat channels: Game/Role/Instructor channels
- Real-time multiplayer: WebSocket updates
- Touch interactions: Drag and drop orders
- Mobile adaptation: Vertical layout for <768px

---

**Generate a fully functional, production-ready React component matching this specification exactly. The game board should visually match the reference image layout with the inventory facility, corner slots, pipeline Week slots, and green flow arrows.**
