# Task 4: Dice Roller & History
## Objective: Handle POST submissions, simple state, and summarizing results. Core Requirements:

- [ ] Form to submit number of dice and sides; shows current roll results and a history of the last X rolls.
- [ ] Display aggregate statistics (min, max, average, frequency distribution). Constraints:
- [ ] Enforce safe ranges for dice count and sides.
- [ ] Prevent duplicate form re-submission (use redirect-after-post pattern). Stretch Ideas:
- [ ] Visualize frequencies with proportional bars (using Bootstrap utilities).
- [ ] Add a mode that “locks” certain dice values for next roll (simulated). Reflection Prompts:
- [ ] Why is redirect-after-post important here?
- [ ] How did you design the data structure for history?