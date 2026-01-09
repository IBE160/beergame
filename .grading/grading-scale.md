## Method 1 (most common): Convert letters → points, take a weighted average, convert back

1. **Choose a numeric scale** for A–F (example):

   - A = 5
   - B = 4
   - C = 3
   - D = 2
   - E = 1
   - F = 0

2. **Compute weighted score**

   $$S = 0.30 \cdot p_1 + 0.40 \cdot p_2 + 0.30 \cdot p_3$$

   where $p_1, p_2, p_3$ are the point values for the three assessments.

3. **Convert score back to a final letter grade** using cutoffs you define.

   Example cutoffs (simple and transparent):

   - A if $S \ge 4.5$
   - B if $3.5 \le S < 4.5$
   - C if $2.5 \le S < 3.5$
   - D if $1.5 \le S < 2.5$
   - E if $0.5 \le S < 1.5$
   - F if $S < 0.5$

**Example:** (B, C, A) = (4, 3, 5)

$$S = 0.30 \cdot 4 + 0.40 \cdot 3 + 0.30 \cdot 5 = 1.2 + 1.2 + 1.5 = 3.9 \Rightarrow \text{B}$$

**Pros:** consistent, easy in Excel/LMS, defensible.
