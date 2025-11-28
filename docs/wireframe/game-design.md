# Retailer Game Board - Logic Analysis

## Overview

The `retailer-game-board-beergame.html` wireframe is a Beer Game supply chain simulation dashboard for the **Retailer** role. It demonstrates a turn-based game with animated supply chain flows between Wholesaler, Retailer, and Customers.

## Layout Structure

### Three Main Nodes (Left to Right on Desktop, Top to Bottom on Mobile)
1. **Wholesaler Node** (upstream supplier)
   - Hidden inventory display (information asymmetry)
   - Order slot (receives orders from retailer)

2. **Retailer Node** (player's role - center)
   - Visible inventory display (50 units initial)
   - Order input with up/down buttons and Send button
   - Demand slot (receives customer demand)

3. **Customer Node** (downstream demand)
   - Person icons representing market
   - Random demand generation (10-20 range)
   - Demand display showing "?"

### Pipe Sections (Desktop: Horizontal, Mobile: Vertical)

**Wholesaler -> Retailer Pipe:**
- **Green Delivery Boxes**: Week 1 and Week 2 slots (incoming deliveries from wholesaler)
- **Yellow Order Pipe**: Orders flowing from retailer to wholesaler

**Retailer -> Customer Pipe:**
- **Yellow/Accent Outgoing Boxes**: Week 1 and Week 2 slots (outgoing deliveries to customers)
- **Red Demand Pipe**: Demand flowing from customers to retailer

## Shared Game State

```javascript
const gameState = {
    config: {
        wholesalerInventory: 100,
        demandRange: { min: 10, max: 20 }
    },
    demand: 0,
    orderValue: 0,
    retailerInventory: 50,
    wholesalerDelivery: 0,
    retailerOutgoing: 0,
    greenWeek1: 20,  // Incoming delivery week 1
    greenWeek2: 30,  // Incoming delivery week 2
    yellowWeek1: 25, // Outgoing delivery week 1
    yellowWeek2: 20, // Outgoing delivery week 2
    phase2: { deliveryClone: null, outgoingClone: null }
}
```

## Key Game Methods

1. **generateDemand()**: Random demand between 10-20
2. **calculateDelivery(available, requested)**: `Math.min(Math.max(0, available), Math.max(0, requested))`
3. **processWholesalerOrder(orderValue)**: Calculates wholesaler delivery based on available inventory
4. **processRetailerDemand(demandValue)**: Updates retailer inventory and calculates outgoing delivery
5. **receiveDelivery(amount)**: Adds delivery to retailer inventory
6. **advanceWeeks()**: Shifts week slot values (Week 1 -> Week 2, new values enter Week 1)

## Animation Phases (Mobile)

### Phase 1 (Parallel animations - 2 seconds)
1. Customer Demand -> Retailer Demand slot (vertical down)
2. Retailer Order -> Wholesaler Order slot (vertical down)
3. Outgoing Week 2 -> Customer icons (up then right, fades out)
4. Outgoing Week 1 -> Week 2 slot (vertical up)
5. Green Delivery Week 2 -> Retailer Inventory (down then right, fades in)
6. Green Delivery Week 1 -> Week 2 slot (vertical down)

### Phase 2 (After 1s pause - 2 seconds)
1. Wholesaler Order -> Wholesaler Inventory (horizontal left, morphs yellow to green)
2. Retailer Demand -> Retailer Inventory (left then down, morphs red to yellow)

### Phase 3 (After 1s pause - 2 seconds)
1. Green delivery slot (from Phase 2) -> Week 1 slot (right then up)
2. Yellow outgoing slot (from Phase 2) -> Outgoing Week 1 slot (right then up)

## Animation Phases (Desktop)

Similar logic but with horizontal flow directions:
- Deliveries flow rightward (Wholesaler -> Retailer -> Customer)
- Orders/Demand flow leftward (Customer -> Retailer -> Wholesaler)

## Clone Animation Helper

The `animateClone()` function supports multiple path types:
- `direct`: Straight line
- `dogleg`: Horizontal first, then vertical
- `vertical-dogleg`: Vertical first, then horizontal
- `vertical-align-y`: Vertical only
- `horizontal`: Horizontal only
- `vertical-down`: For mobile deliveries
- `vertical-up`: For mobile orders

## Charts Section (React/Recharts)

### Data Simulation
- 10 weeks of simulated data
- Initial inventory: 50 units
- Holding cost: $10/unit/week
- Backorder cost: $20/unit/week

### Charts Displayed
1. **Orders vs. Inventory Chart** (ComposedChart)
   - Bar: Outgoing orders
   - Line: Inventory level
   - Line: Backorders

2. **Cost Accumulation Chart** (AreaChart)
   - Stacked areas: Cumulative holding cost + backorder cost

3. **Metrics Panel**
   - Total Cost (cumulative)
   - Service Level (% of fully delivered orders)
   - Fill Rate (delivered/demanded ratio)

4. **Statistics Panel**
   - Central Tendency: Mean, Median, Mode
   - Dispersion: Min, Max, Range, Std Dev
   - Distribution: CV, Skewness, Kurtosis, IQR
   - Inference: Std Error, Margin, 95% CI

## Key UI States

1. **State 1**: Input enabled, order can be entered
2. **State 2**: After clicking Send, button shows "WAIT" then "SENT", inputs disabled
3. **State 3**: Animations play showing supply chain flows
4. **State 4**: UI re-enabled after animations complete (9 seconds on mobile)

## Responsive Design

- **Desktop (lg: 1024px+)**: Horizontal layout, left-to-right flow
- **Mobile (<1024px)**: Vertical layout, top-to-bottom flow
- Uses Tailwind's `lg:` prefix for responsive breakpoints
- `isMobile()` function checks `window.innerWidth < 1024`

## CSS/Styling

- Dark theme with monochromatic colors
- Accent color: Gold (#FFD700)
- Green for incoming deliveries
- Yellow/Accent for outgoing deliveries
- Red for demand
- Tailwind CSS with custom configuration
- Material Symbols for icons
