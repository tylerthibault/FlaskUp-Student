# Task 1: Dynamic Grid (Foundations)


## Objective: Practice reading query parameters and rendering dynamic structure with nested loops. Core Requirements:

- [x] Route renders a grid with default dimensions (e.g., 3x3) overridden by query params (rows, cols).
- [x] Each cell displays its coordinates or ordinal number.
- [ ] A simple form (GET) at the top allows regenerating the grid. Constraints:
- [ ] Must validate rows/cols as positive integers with sane max limits (prevent enormous grids).
- [ ] Provide a user-friendly message if validation fails and fall back to defaults. Stretch Ideas:
- [ ] Add a selectable color theme (one variable affecting all cells).
- [ ] Add an optional “numbered” vs “coordinate” display mode. Reflection Prompts:
- [ ] What assumptions did you enforce about user input?
- [ ] Where did you draw the line between view logic and template presentation?