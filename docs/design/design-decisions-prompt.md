# Prompt Template: UI Design Spec (Skills 1–3 Only)

## Table of Contents

1. [Role & Objective](#1-role--objective)  
2. [Required Reading & Research](#2-required-reading--research)  
3. [Project Context](#3-project-context)  
4. [Tasks Overview](#4-tasks-overview)  
5. [Typography Spec (Skill #1)](#5-typography-spec-skill-1)  
   5.1 [Picking Fonts](#51-picking-fonts)  
   5.2 [Setting Up the Type System](#52-setting-up-the-type-system)  
6. [Layout Spec (Skill #2)](#6-layout-spec-skill-2)  
   6.1 [Columns & Grids](#61-columns--grids)  
   6.2 [Spacing System](#62-spacing-system)  
   6.3 [Visual Hierarchy](#63-visual-hierarchy)  
7. [Color Spec (Skill #3)](#7-color-spec-skill-3)  
   7.1 [Limiting the Palette](#71-limiting-the-palette)  
   7.2 [Opacity & Variations](#72-opacity--variations)  
   7.3 [Contrast & Accessibility](#73-contrast--accessibility)  
   7.4 [Palette Sourcing & Curation](#74-palette-sourcing--curation)  
8. [Output Format](#8-output-format)  
9. [Style & Constraints](#9-style--constraints)

---

## 1. Role & Objective

You are an expert **product designer + UI/UX designer**.

Your job is to create a **UI design specification** for a web-based product focusing only on:

1. **Typography** (Skill #1)  
2. **Layout** (Skill #2)  
3. **Color** (Skill #3)  

You must **explicitly ignore and not use** Skill #4 and Skill #5 from the source article.

---

## 2. Required Reading & Research

1. Carefully read this article in full:

   - **“The Only 5 Skills Required for a Web Designer (That Actually Matter)”**  
     - URL: `https://selfmadewebdesigner.com/the-only-5-skills-required-for-a-web-designer-that-actually-matter/`

2. From that article, use only the content under:

   - **Skill #1: Typography**, especially:
     - How to pick the right fonts.
     - How to set up fonts: font sizes, letter spacing, and line height (type scale system).
   - **Skill #2: Layout**, especially:
     - Rule #1: Use columns & grids (12/8/4).
     - Rule #2: Master spacing (8-point grid, whitespace, “double between sections” rule).
     - Rule #3: Create visual hierarchy (proximity, size, contrast, alignment).
   - **Skill #3: Color**, especially:
     - Limit your palette.
     - Use opacity instead of new colors.
     - Prioritize contrast.
     - Don’t design palettes from scratch—curate and refine.

3. Use web search / browsing tools to cross-check and, if needed, refine:

   - Current best practices for:
     - **UI typography** (type scales, minimum font sizes, line-height ranges).
     - **Responsive layout systems** (12-column grids, 8pt spacing).
     - **Color & accessibility** (WCAG 2.1 AA contrast requirements).
   - You may reference ideas from well-known design systems (e.g., Material Design, Apple HIG) as inspiration, but keep the spec system-agnostic.

---

## 3. Project Context

The user will provide a short description of the product.

Use this section as a placeholder for that description:

> **Product Description (provided by user):**  
> [Briefly describe the product here: target users, main purpose, key pages or flows, brand tone, and constraints.]

Your entire UI design spec must be tailored to this specific product context while still following Skills 1–3 from the article.

---

## 4. Tasks Overview

Create a **UI Design Specification** structured into three main sections:

1. **Typography Spec (Skill #1)**  
2. **Layout Spec (Skill #2)**  
3. **Color Spec (Skill #3)**  

Each section must follow the subtask breakdown from the article:

- Typography → “Pick fonts” + “Set up fonts (sizes, letter spacing, line height)”.
- Layout → “Columns & grids”, “Spacing”, “Visual hierarchy”.
- Color → “Limit palette”, “Use opacity”, “Prioritize contrast”, “Curate palettes”.

---

## 5. Typography Spec (Skill #1)

Base this entirely on the **Typography** section of the article, expanded with best practices.

### 5.1 Picking Fonts

Define:

- **Primary UI font family** (for headings, body, buttons, navigation).
- Optional **secondary / numeric font** (for dense data, code, or KPIs).
- Rules for:
  - How many fonts are allowed (e.g., primary + optional numeric).
  - When to use each font (headlines vs body vs numeric).
  - Criteria for choosing fonts (legibility, x-height, style fit with brand, licensing).

Include:

- Guidance on how to avoid overused / default fonts where appropriate.
- Suggestions for using curated font sources (e.g., modern free font libraries or established web fonts) without naming specific libraries if not needed.

### 5.2 Setting Up the Type System

Define a **type scale system** as described in the article:

- Start from a **base font size** for paragraph text (e.g., 16px).
- Choose a **ratio** (e.g., Major Third 1.25) to derive heading sizes.
- Present a **table** of type tokens, for example:

  - Base body text
  - Small text / labels
  - Captions
  - H1–H4 (or up to H6 if relevant)
  - KPI / numeric styles

For each type level, specify:

- Font size (in px and rem if useful).
- Line-height guidelines.
- Letter-spacing guidelines:
  - Body text: default letter-spacing (as per article: “don’t touch it”).
  - Larger headings: increasingly tighter tracking as size increases.

Also include:

- Accessibility notes:
  - Minimum recommended body size.
  - How line-height should change with font size (e.g., ~150% for body, shrinking slightly as text gets larger).
  - Considerations for long-form text vs dashboards vs mobile.

---

## 6. Layout Spec (Skill #2)

Base this entirely on the **Layout** section of the article, expanded with best practices.

### 6.1 Columns & Grids

Define a responsive grid system:

- **Desktop:** typical use of a 12-column grid.
- **Tablet:** typical use of an 8-column grid.
- **Mobile:** typical use of a 4-column grid.

For each breakpoint, specify:

- Column count.
- Typical gutter sizes.
- How to break the columns into common layouts (e.g., 2/3/4-column sections, sidebars, content + aside).

Explain:

- Why the grid matters for consistent alignment and structure.
- How to apply grids to:
  - Page shells (headers, nav, content).
  - Key product screens (e.g., dashboards, forms, content-heavy pages).

### 6.2 Spacing System

Define a **spacing system** inspired by the **8-point grid** from the article:

- List spacing tokens (e.g., 4, 8, 12, 16, 24, 32, 40, 48, 64 px).
- Explain how these apply to:
  - Padding inside cards, panels, and sections.
  - Margins between components.
  - Vertical rhythm between sections.

Include the article’s rule-of-thumb:

- **Double the spacing** between sections compared to the spacing inside sections.
  - Example: 16px inside a section → 32px between this section and the next.

Clarify:

- How to use spacing to create “breathing room”.
- How to avoid overcrowding and visual noise.

### 6.3 Visual Hierarchy

Define rules for visual hierarchy using the principles from the article:

- **Proximity:**  
  - Keep related elements close (e.g., headings with their paragraphs, labels with fields).
- **Size:**  
  - Larger = more important; define which elements get the largest sizes.
- **Contrast:**  
  - Use color, weight, and size differences to highlight key content (but don’t rely on color alone).
- **Alignment:**  
  - Maintain consistent, intentional alignment lines to guide the eye.

Describe:

- How to guide scanning from **most important** to **least important** elements on typical product pages (e.g., hero sections, dashboards, detail pages).
- How to use hierarchy to clarify key actions, key information, and secondary details.

---

## 7. Color Spec (Skill #3)

Base this entirely on the **Color** section of the article, expanded with best practices.

### 7.1 Limiting the Palette

Define a simple base color system:

- **Neutrals** (backgrounds, surfaces, body text).
- **Primary** color (brand / main highlight).
- **Secondary** color (supporting surfaces or accents).
- **Accent** color (key CTAs, highlights).

Explain a **distribution rule** such as the 60/30/10 pattern:

- ~60% neutrals.
- ~30% primary/secondary.
- ~10% accent.

Describe:

- Typical uses for each role (backgrounds, buttons, links, alerts, etc.).
- How to avoid overusing accent colors.

### 7.2 Opacity & Variations

Describe how to **reuse colors via opacity** instead of introducing many new colors:

- Use tints/shades of the primary/secondary colors by adjusting opacity.
- Apply these to:
  - Backgrounds of cards and panels.
  - Chart fills and subtle highlights.
  - Hover/pressed states.

Explain:

- Why this reduces palette complexity and increases harmony.
- When to prefer opacity vs a separate token color.

### 7.3 Contrast & Accessibility

Define contrast requirements inspired by the article and WCAG:

- Minimum contrast ratios for:
  - Normal text vs background.
  - Large text vs background.
- Contrast requirements for:
  - Buttons, form controls, and interactive elements.
  - Focus states and hover states (visible and distinct).

Include:

- Recommendation to use automated contrast checking tools.
- A clear rule: aesthetics must not override legibility.

### 7.4 Palette Sourcing & Curation

Explain how to **curate** palettes instead of designing from scratch:

- Strategies:
  - Deriving palettes from existing brand materials or reference sites.
  - Using curated palette tools as a starting point.
- Guidance:
  - How to evaluate whether a palette fits the project’s tone and audience.
  - How to adjust / refine borrowed palettes (e.g., tweak saturation, brightness, or contrast).

---

## 8. Output Format

Return the final answer as a **Markdown document** with this structure:

- `# UI Design Spec (Skills 1–3)`  
- `## 1. Typography`  
- `## 2. Layout`  
- `## 3. Color`  

Within each section:

- Use nested headings (e.g., 1.1, 1.2, etc.) matching the subtasks above.
- Use bullet points, short paragraphs, and small tables where helpful.
- Make the spec implementation-friendly (easy to translate into design tokens or CSS/Tailwind variables).

---

## 9. Style & Constraints

- Be **concise but concrete**:
  - No long-winded theory; focus on practical decisions and rules.
- Always align with:
  - Skill #1: typography focus from the article.
  - Skill #2: layout focus from the article.
  - Skill #3: color focus from the article.
- Do **not** reference or use:
  - Skill #4 (Code).
  - Skill #5 (Conversion thinking).
- Keep the spec:
  - **System-agnostic** (no specific framework code).
  - **Product-specific**, based on the user’s description in the “Project Context” section.
