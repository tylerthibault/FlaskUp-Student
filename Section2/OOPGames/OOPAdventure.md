# OOP Text Adventure Game Assignments

Design a series of assignments for building a text adventure game in Python using OOP principles. Each assignment increases in difficulty, allowing learners to progressively build skills and create a more complex game.

---

## Level 1: Basic Room Navigation

**Objective:**  
Create a simple text adventure game where the player can move between rooms.

**Instructions:**
- Create a `Room` class with a name and description.
- Create a `Player` class with a current location.
- Set up several rooms and link them together (e.g., north, south, east, west).
- Allow the player to type commands to move between rooms.
- Print the current room’s description after each move.

**Stretch:**  
Add a simple map display or allow "look" commands for room details.

---

## Level 2: Items and Inventory

**Objective:**  
Add items to rooms and allow players to collect and use them.

**Instructions:**
- Create an `Item` class with a name and description.
- Place items in rooms.
- Add an inventory to the `Player`.
- Allow commands like "take [item]" and "use [item]".
- Print inventory contents when requested.

**Stretch:**  
Add items that unlock new rooms or solve simple puzzles.

---

## Level 3: Non-Player Characters (NPCs) and Interaction

**Objective:**  
Add characters that the player can talk to or trade with.

**Instructions:**
- Create an `NPC` class with dialogue and possible actions.
- Place NPCs in rooms.
- Allow the player to interact with NPCs via commands (e.g., "talk [npc]", "trade [npc]").
- NPCs may give hints, items, or quests.

**Stretch:**  
Add quests or simple branching dialogue trees.

---

## Level 4: Puzzles and Game Logic

**Objective:**  
Implement puzzles or obstacles that must be solved to progress.

**Instructions:**
- Add locked doors, riddles, or other challenges.
- Some items or actions should be required to solve puzzles.
- Use class methods to handle puzzle logic.
- Track player progress and puzzle states.

**Stretch:**  
Add multiple puzzle types and a scoring system.

---

## Level 5: Combat System

**Objective:**  
Add a simple combat system with enemies.

**Instructions:**
- Create an `Enemy` class with health, attacks, and possible loot.
- Allow the player to fight enemies using commands.
- Implement basic health and damage mechanics.
- Award items or points for defeating enemies.

**Stretch:**  
Include player stats, enemy variety, and special abilities.

---

## Level 6: Save/Load Feature and Game Victory

**Objective:**  
Allow the player to save and load their progress; implement a win condition.

**Instructions:**
- Serialize the game state (player, inventory, rooms, etc.) for saving/loading.
- Add a victory condition (e.g., collect a treasure, escape the dungeon).
- Display end-game messages for win or loss.

**Stretch:**  
Implement autosave or multiple save slots.

---

## Level 7: Advanced World and Events

**Objective:**  
Create a dynamic world with events and time progression.

**Instructions:**
- Add a game clock or turn counter.
- Trigger events based on time or player actions (e.g., NPCs move, doors lock/unlock).
- Use inheritance for different room, item, and character types.
- Add random events and replayability.

**Stretch:**  
Support multiple endings or story branches.

---

## Extra Challenges (For Advanced Learners)

- Implement a graphical or web interface.
- Add sound effects or animations.
- Support multiplayer or AI players.
- Build a level editor for custom adventures.

---

Each assignment can be used as a standalone project or built sequentially for a deeper, more complex game!