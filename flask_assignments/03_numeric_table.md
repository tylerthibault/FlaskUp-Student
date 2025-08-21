Below is an expanded, implementation‑oriented description of Task 3 without any code, giving your student more structure, vocabulary, and clear acceptance criteria.

--------------------------------------------------
Task 3: Numeric Table (Multiplication / Addition Table)
--------------------------------------------------

High‑Level Goal:
Build a dynamic N x N numeric table whose contents are derived from two loop indices and an operation mode (e.g., multiply or add). This reinforces: query parameter handling, validation, preparing derived data in the view (not in the template), semantic HTML table structure, and visually communicating state (active operation, headers, optional modes).

Core User Story:
“As a user, I can request a numeric table of size N (with safe limits) and pick an operation mode so I can explore numeric relationships (e.g., multiplication or addition) with clear headers and visual cues.”

Primary Features (Rephrased & Expanded):
1. Table Size Control:
   - Query parameter (e.g., n) defines dimension (N x N).
   - Uses a sensible default when missing or invalid.
   - Enforced upper bound to prevent rendering performance or huge layout scroll.
2. Operation Modes:
   - At least two modes (e.g., multiply, add) selected via query parameter.
   - Active mode is visually indicated (e.g., a label, highlighted choice, or textual banner).
3. Table Semantics:
   - First row and first column function as headers (conceptually “factors” or “operands”).
   - Distinguish header cells from data cells (semantic structure).
4. Derived Values:
   - Each non‑header cell computed based on row and column indices and current operation.
   - Computation is performed in Python (view/controller layer), not inside the template logic body (template should only loop & display prepared structures).
5. Validation & Feedback:
   - If user supplies out‑of‑range or non‑numeric N, fallback to default and present a user‑friendly notice of what happened (not a crash).
   - Invalid or unsupported operation mode falls back to a default mode (communicate fallback).

Constraints Clarified:
- Max N: Pick and clearly document an upper bound (example: 30 or 50). This number should be a constant defined centrally (no “magic numbers” scattered).
- Visual communication: The current operation mode must be obvious without reading query parameters (e.g., a highlighted tab, badge, or heading text).
- Logic Separation: All numeric generation logic belongs outside the template loops (e.g., precomputed 2D structure passed into the template). The template’s responsibility: iterate and render.

Stretch Features (Detailed):
1. Cell Hover Highlight:
   - When hovering over a data cell, highlight the entire row and column so patterns are clearer (pure CSS or simple class approach).
   - Accessibility note: ensure hover highlight has sufficient contrast; consider keyboard focus parity if you later add interactive cells.
2. Diagonal‑Only Toggle:
   - Query parameter (e.g., diagonal=1) causing non‑diagonal cells to appear visually muted (e.g., greyed).
   - Still show all values (so the table does not change layout), but visually de‑emphasize non‑diagonal.
   - Clarify whether diagonal includes both first row/column headers or only intersection cells (decide and document).

Extended Ideas (Optional, Not Required):
- Mode Explanations: Provide a short textual explanation for each mode (e.g., “Multiplication: cell = row_value * column_value”).
- Additional Operations: subtraction (col − row), exponent (row^col) with caution about large numbers, or modulo. Each requires validation & potential constraints (e.g., avoid huge exponents).
- Color Scaling: Optionally map result magnitude to a color intensity scale (requires careful legend and accessible contrast).
- Export Option (concept only): Indicate how user could add a download (CSV) later.

Data Design / Structures (Conceptual — No Code):
- Decide a single structured data object passed to the template:
  - Table metadata: size N, operation name, operation symbol, headers list.
  - 2D array of cell objects or plain numbers (plus optional flags like is_diagonal).
  - Validation messages list (empty if everything ok).
- Centralize constants: DEFAULT_N, MAX_N, SUPPORTED_OPERATIONS (mapping keys to labels & functions), DEFAULT_OPERATION.

Validation Rules (Spell Them Out):
1. n missing => use DEFAULT_N.
2. n not integer => fallback + notice.
3. n < 1 => fallback + notice.
4. n > MAX_N => clamp or fallback + notice (choose one strategy; document).
5. operation missing or unsupported => fallback to DEFAULT_OPERATION + notice.
6. (Stretch) diagonal parameter: only accept “1”/“true”/“yes” (pick one canonical parsing strategy), else treat as off.

State Communication:
- Validation messages presented in a consistent spot (e.g., top of page).
- Active operation visually distinct (avoid ambiguous text only differences).
- If diagonal mode is on, show a brief indicator or legend.

Preventing Magic Numbers:
- Use clearly named constants for:
  - DEFAULT_N
  - MAX_N
  - Allowed operations set
  - (Optional) HOVER_HIGHLIGHT_ENABLED (if gating)
- Document these constants in a small readme section for this task.

Performance Considerations:
- Complexity is O(N^2); with N <= MAX_N you guarantee acceptable render time.
- Consider page weight: large tables produce many DOM nodes; justify MAX_N accordingly.

Accessibility & Semantics:
- Use appropriate table header semantics (first row and first column). Decide whether the top-left corner cell is a header placeholder (e.g., blank or label).
- Provide a caption or label describing what the table represents (e.g., “12 x 12 Multiplication Table”).
- If using color scaling or greyed diagonal, ensure non-color cues (e.g., subtle symbol or cell attribute) if accessibility is a focus.

Error & Fallback Messaging Guidelines:
- Use clear, concise language (“Requested size 0 is invalid; reverted to default size 10.”).
- Distinguish multiple messages if more than one parameter is invalid.
- Keep messages neutral/informative (no blame).

Testing / Acceptance Checklist:
1. Default load (no params) shows expected default N and default operation.
2. Valid n + valid operation renders correct dimensions and correct sample calculations.
3. Out-of-range n triggers fallback message and uses safe value.
4. Non-numeric n triggers fallback.
5. Unsupported operation triggers fallback with notice.
6. First row & column styled distinctly.
7. Active operation visible at a glance.
8. (Stretch) Hover highlight works for multiple cells, row & column highlight consistent.
9. (Stretch) Diagonal-only toggle: diagonal cells appear normal, others de-emphasized.
10. No computation logic leaks into template beyond simple referencing of prepared values.

Reflection Prompts (Expanded Guidance):
1. “How did you prevent magic numbers?”
   - Expect the student to mention named constants and centralized configuration rather than scattered literals.
2. “How would you extend to support custom user-defined operations safely?”
   - Points to cover: whitelist vs executing arbitrary expressions, security risks of evaluation, potential mapping of symbolic names to pre-defined safe functions, optional argument constraints (e.g., limiting exponent growth), and validation that rejects unknown symbols.

Documentation Expectations:
- Brief explanation of supported query parameters with examples:
  - Example URL patterns (e.g., /table?n=12&op=mul).
- Section describing each operation’s formula.
- Explanation of diagonal mode if implemented.
- Observed limitations (e.g., why MAX_N chosen).
- Reflection answers appended at bottom.

Potential Pitfalls to Warn Against:
- Performing string parsing or math inline in the template repeatedly (inefficient and mixes concerns).
- Failing to sanitize user operation leading to arbitrary code evaluation (if they’re tempted to implement user-entered formulas).
- Unclear or duplicated code for building header labels.
- Forgetting to handle integer conversion errors gracefully.
- Allowing coloring logic to creep into multiple places rather than centralizing.

Extension Path to Future Tasks:
- The pattern of: validate parameters -> compute structured data -> pass to template sets precedent for future features (dice stats, filtering, etc.).
- Introduces mindset of mapping keys to display names (operation map), which parallels later tasks with filtering/sorting.

Open Design Decisions (Student Must Resolve & Document):
1. Should invalid n clamp to MAX_N or revert entirely to DEFAULT_N?
2. What is the top-left corner header cell content (blank, symbol, label)?
3. How are operation choices displayed (tabs, radio inputs, links)?
4. How are multiple validation messages ordered (chronological, priority)?
5. If diagonal mode is on, should headers still behave unchanged or also be visually altered?

Evaluation Rubric (Specific to This Task):
- Input Handling (0–5): correct fallback, clear messages.
- Semantic Structure (0–5): proper header semantics, caption, accessible labeling.
- Logic Separation (0–5): minimal logic in template; clear data structure.
- Visual Communication (0–5): active mode + headers + optional diagonal clear.
- Extensibility (0–5): easy to add new operations; no duplication.
- Documentation & Reflection (0–5): clarity, completeness, insight.

Deliverables Recap:
- Working route and template (no code in this brief, but student will implement).
- README section describing parameters, behaviors, constraints.
- Screenshot of default table + one alternate mode.
- Reflection answering both prompts.
- (If stretch done) second screenshot showing diagonal or hover effect.

You can copy this expanded description directly to the student. If you’d like, I can produce similarly expanded briefs for later tasks—just specify which task number next. Let me know how you’d like to proceed.