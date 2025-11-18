# Beer Game UI Design Spec  
_Focus: Typography, Layout, Color (Skills 1–3)_

This spec guides UI design for the Beer Game platform (all tiers), with emphasis on the **Game Dashboard** and **Instructor** views.

---

## 1. Typography

### 1.1 Font Families

- **Primary UI font**
  - `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`
  - Used for: headings, body text, buttons, inputs, nav, chat.
- **Numeric/Data font**
  - Use primary font with tabular numbers _or_ a monospace:
  - `"JetBrains Mono", "Roboto Mono", monospace`
  - Used for: KPIs, table numbers, chart labels if needed.

> Rule: Max 1 primary + 1 numeric/mono family. No decorative fonts.

### 1.2 Type Scale (Desktop/Laptop)

Base body: `16px` (`1rem`), line-height `1.5`.

| Token       | Use                                   | Size | Line-height | Letter-spacing |
|------------|----------------------------------------|------|-------------|----------------|
| `text-h1`  | Page / main section title             | 40px | 1.2         | -0.02em        |
| `text-h2`  | Dashboard / panel titles              | 32px | 1.25        | -0.015em       |
| `text-h3`  | Card / component headings             | 24px | 1.3         | -0.015em       |
| `text-h4`  | Subheadings, chart titles             | 20px | 1.3         | -0.01em        |
| `text-body`| Body text, chat messages              | 16px | 1.5         | 0              |
| `text-sm`  | Labels, table headers                 | 14px | 1.4         | 0              |
| `text-xs`  | Captions, helper text, chip labels    | 12px | 1.4         | 0              |

- Mobile/tablet: scale headings down one step (e.g., H1 → `text-h2`).

### 1.3 Usage Guidelines

- **Game dashboard**
  - Top: `H2` — “Retailer · Week 7 of 20”.
  - Inventory/Backorder labels: `text-sm`, values: `text-body` or `text-h4` (for emphasis).
- **Instructor analytics**
  - Class title: `H1`.
  - Tabs (“Monitoring”, “Analytics”, “Assessments”): `text-body` or `text-h4`.
  - Table cells: `text-body`; headers: `text-sm`.

---

## 2. Layout

### 2.1 Grids

- **Desktop (≥ 1280px)**
  - 12-column grid, gutter: 24px.
- **Laptop (1024–1279px)**
  - 12-column grid, gutter: 16–24px.
- **Tablet (768–1023px)**
  - 8-column grid, gutter: 16px.

**Dashboard example (desktop):**

- Left sidebar (nav between Board/Data/Results/Exercises): **2–3 columns**.
- Main game board: **6–7 columns**.
- Right chat sidebar: **3–4 columns**, collapsible.

### 2.2 Spacing (8pt System)

Use multiples of 4/8px for ALL spacing.

- Tokens:
  - `4, 8, 12, 16, 24, 32, 40, 48, 64` px.
- Guidelines:
  - Card/panel padding: `16–24px`.
  - Gap between items inside a panel: `8–16px`.
  - Gap between major sections: ~2× inner spacing (e.g. 32px if inner gap is 16px).

### 2.3 Hierarchy & Placement

- **Priority order (Game Dashboard):**
  1. Role + week + key KPIs (Total Cost, Inventory, Backorders).
  2. Game board (inventory + facilities, decision input).
  3. Charts + statistics.
  4. Data table, chat, secondary details.

- **Alignment:**
  - Panels aligned to grid columns.
  - Table labels left-aligned; numeric values right-aligned.
  - Chart titles aligned to chart left; legends consistent across charts.

### 2.4 Key Components

- **Game board**
  - Central inventory rectangle:
    - Corner slots: Incoming/Outgoing Order/Delivery (4 mini-panels).
    - Center: “Inventory” label + value (positive/negative).
  - Factory: production facility above, transport pipeline below.
  - Wholesaler/Distributor: transport pipelines above/below delivery slots.
  - Retailer: inbound pipeline above, arrows to/from customer.

- **Chat sidebar**
  - Right side; collapsible.
  - Collapsed: vertical icon bar for main channels.
  - Expanded: channel list + messages + input at bottom.

- **Results/Exercises**
  - In Results view: main multi-role charts on top, role-specific charts/statistics below.
  - In Exercises view: list of exercises with clear scoring and feedback panels.

---

## 3. Color

### 3.1 Palette Structure

Use a **60/30/10** rule: 60% neutral, 30% primary, 10% accent.

- **Neutrals**
  - `neutral-0`: #FFFFFF (page background)
  - `neutral-50`: very light gray (card bg)
  - `neutral-500`: body text
  - `neutral-700`: headings
  - `neutral-900`: high-emphasis text
- **Primary**
  - Brand color (e.g. a calm blue) for:
    - Main nav, active tabs, primary chart lines.
- **Accent**
  - High-contrast color (e.g., teal or amber) for:
    - Primary CTAs, important highlights.

- **Semantic colors**
  - Positive (inventory OK, good score): green.
  - Negative (backorders, errors): red.
  - Warning: amber.
  - Info: muted blue.

### 3.2 Accessibility

- Text contrast:
  - Normal text: ≥ 4.5:1 vs background.
  - Large text (≥ 18pt or 14pt bold): ≥ 3:1.
- Interactive components:
  - Buttons, inputs, and controls: ≥ 3:1 vs adjacent colors.
- Never rely on color alone:
  - Combine color with icons/labels (e.g. “Error”, “Pass”, “Fail”).

### 3.3 Component Color Rules

- **Game board**
  - Inventory value:
    - Positive: green text (or chip) on neutral bg.
    - Negative: red text and/or subtle red-tinted bg.
  - Arrows: neutral/primary line color; direction indicated by shape, not just color.

- **Charts**
  - During game:
    - Player’s outgoing orders: primary color (line or bar).
    - Inventory/backorders: secondary hues of blue/green.
  - After game:
    - Role colors:
      - Retailer: blue
      - Wholesaler: green
      - Distributor: purple
      - Factory: orange
    - Customer demand: dark neutral.
    - Supply chain stacked cost: tints of role colors.

- **Chat**
  - Background: neutral-0 or neutral-50.
  - Player messages: accent or primary bubble with white text.
  - Others: neutral bubbles with dark text.
  - AI messages: tinted bg + “AI” badge/icon.

- **Analytics & assessments**
  - Best performers: light green row highlight + up-arrow.
  - Worst performers: light red row highlight + down-arrow.
  - Thresholds (e.g., passing score): accent line in charts.

### 3.4 Opacity Strategy

Prefer opacity over new colors:

- Secondary panel bgs: primary color at 4–8% opacity.
- Chart area fills: same hue, 20–40% opacity.
- Hover states: slightly increased opacity or a subtle tint of existing colors.

---

## 4. Implementation Notes

- Map all sizes, colors, and spacing to design tokens:
  - Tailwind config (fontSize, lineHeight, spacing, colors).
  - Shadcn theme overrides (typography, button, card, tabs).
- Use the same system across:
  - Landing pages
  - Game dashboard
  - Instructor dashboards
  - Assessments & analytics

