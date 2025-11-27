# Plan: Fix Retailer Game Board Animation & Sizing (Desktop + Mobile)

## Problem Summary

The retailer game board (`retailer-game-board-beergame.html`) has a responsive layout that switches between:
- **Mobile/Tablet (<780px):** Vertical flow with vertical connector pipes
- **Desktop (≥780px):** Horizontal flow with horizontal connector pipes

**Issues identified:**

1. **Animation doesn't work in desktop mode** - The animation code's `isMobile()` function checks `window.innerWidth < 640` but the layout breakpoint is `780px`. This causes animations to run with wrong layout assumptions.

2. **Sizing inconsistencies with wholesaler reference** - The desktop layout doesn't match the wholesaler game board's proportions and spacing.

3. **No vertical animations for mobile** - Currently mobile just updates values instantly; user wants animated transitions for vertical layout too.

## Root Cause

The layout switches at `min-[780px]` (780px breakpoint) but the JavaScript `isMobile()` function uses `window.innerWidth < 640`. This creates broken behavior in the 640-779px range.

## Recommended Approach

### 1. Fix the Mobile Detection Breakpoint

Change `isMobile()` from `window.innerWidth < 640` to `window.innerWidth < 780` to match the CSS breakpoint.

### 2. Implement Vertical Animations for Mobile Mode

Create new vertical animation paths for the mobile layout:
- **vertical-down**: Animate downward along the left pipe (deliveries)
- **vertical-up**: Animate upward along the right pipe (orders)

The mobile connector pipes use different structure:
- Left pipe: Contains W1/W2 boxes stacked vertically (deliveries flow down)
- Right pipe: Continuous (orders flow up)

Animation sequences for mobile:
1. Order flows UP the right pipe from Retailer → Wholesaler
2. Deliveries flow DOWN the left pipe: W1 → W2 → Retailer Inventory
3. Outgoing deliveries flow DOWN the left pipe: Retailer → W1 → W2 → Customer

### 3. Fix Element Selectors for Responsive Classes

Update selectors to find elements with responsive class variants:
```javascript
// Instead of just '.text-5xl'
els.retailerInventory.querySelector('.text-3xl, .lg\\:text-5xl');
```

### 4. Align Desktop Sizing with Wholesaler Reference

| Component | Current Retailer | Target (Wholesaler) |
|-----------|-----------------|---------------------|
| Node width | `min-[780px]:w-40 lg:w-56` | `min-[780px]:w-56` |
| Pipe min-width | `min-w-[100px] lg:min-w-[200px]` | `min-w-[200px]` |
| Delay box labels | `W1`/`W2` | `Week 1`/`Week 2` |
| Delay box value width | `min-w-[30px]` | `min-w-[55px]` |
| Delay box padding | `p-1` | `p-2` |
| Pipe height | `h-[30px] lg:h-[40px]` | `h-[40px]` |

### 5. Add IDs to Mobile Connector Elements

The mobile vertical connectors need IDs for animation targeting:
- `mobile-delivery-week-1`, `mobile-delivery-week-2`
- `mobile-outgoing-week-1`, `mobile-outgoing-week-2`

## Files to Modify

- `c:\IBE160\projects\beergame\docs\wireframe\retailer-game-board-beergame.html`

## Implementation Steps

### Phase 1: Fix Desktop Animation (Critical)
1. Change `isMobile()` breakpoint to 780px
2. Fix inventory element selector for responsive classes
3. Verify desktop horizontal animations work

### Phase 2: Add Mobile Animation Support
1. Add IDs to mobile connector W1/W2 boxes
2. Add new path types to `animateClone()`:
   - `vertical-down` for deliveries (top to bottom)
   - `vertical-up` for orders (bottom to top)
3. Create `startMobileAnimation()` function with vertical paths
4. Update `startState3Animation()` to call appropriate animation based on layout

### Phase 3: Update Desktop Sizing
1. Update node widths to `min-[780px]:w-56`
2. Update pipe min-widths to `min-w-[200px]`
3. Change delay box labels from `W1`/`W2` to `Week 1`/`Week 2` in desktop
4. Increase delay box padding and value widths
5. Standardize pipe heights to `h-[40px]`

## Animation Path Logic

### Desktop (Horizontal) - Existing
- `direct`: Straight line from source to target
- `dogleg`: Horizontal first, then vertical (for delivery to inventory)
- `vertical-dogleg`: Vertical first, then horizontal
- `horizontal`: Only horizontal movement

### Mobile (Vertical) - New
- `vertical-down`: Move downward, used for deliveries
- `vertical-up`: Move upward, used for orders

## Testing Checklist

- [ ] Desktop (≥780px): Horizontal layout with animations
- [ ] Mobile (<780px): Vertical layout with NEW vertical animations
- [ ] Labels show "Week 1/Week 2" (not abbreviated)
- [ ] Desktop sizing matches wholesaler board
- [ ] Send button triggers animation correctly in both modes
- [ ] Week 1/2 values shift through the pipeline
- [ ] Inventory updates after delivery animation completes
- [ ] Order box values animate to wholesaler in both modes
