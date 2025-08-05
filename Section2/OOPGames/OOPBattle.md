# Progressive OOP Battle Game Assignments

This assignment sequence guides learners through building a battle game in Python using OOP. Each level introduces new concepts and mechanics, increasing the challenge and depth—perfect for progressively building coding and design skills.

---

## Level 1: The Minimal Duel

**Objective:**  
Build the simplest automated battle system.

**Instructions:**
- Create a `Player` class with `name` and `health` attributes.
- Each player has a single attack method that deals fixed damage (e.g., -10 health).
- Instantiate two players and alternate attacks until one is defeated.
- Print health after each attack.

---

## Level 2: Multiple Attacks & User Choice

**Objective:**  
Add attack variety and basic user input.

**Instructions:**
- Expand `Player` with two attack methods (e.g., `attack1`, `attack2`) with different damage.
- Allow the user to control one player, choosing which attack to use each turn.
- The opponent uses random attack selection.
- Print details after each turn.

---

## Level 3: Weapons & Inventory

**Objective:**  
Introduce weapons and inventory management.

**Instructions:**
- Create a `Weapon` class (`name`, `damage`).
- Each player starts with a weapon; attacks use weapon damage.
- Allow players to pick up or swap weapons during the game.
- Print weapon info with each attack.

---

## Level 4: Healing & Potions

**Objective:**  
Add health recovery mechanics.

**Instructions:**
- Create a `Potion` class (`name`, `heal_amount`).
- Players have a limited number of potions in their inventory.
- Players can use a potion on their turn to restore health (up to max).
- Allow user to choose between attacking or healing.
- Opponent uses potions automatically if health is low.

---

## Level 5: Player Stats & Customization

**Objective:**  
Add character stats for deeper gameplay.

**Instructions:**
- Expand `Player` with stats: `strength`, `defense`, `speed`, `luck`.
- Stats influence attack damage, defense against attacks, and special events (e.g., critical hits).
- Let the user customize their player's stats before the game starts.
- Show stats with game messages.

---

## Level 6: Defensive Moves—Blocking & Parrying

**Objective:**  
Introduce defensive choices and chance.

**Instructions:**
- Implement `block` (reduce incoming damage, uses `defense` stat).
- Implement `parry` (chance-based counterattack, uses `speed`/`luck`).
- Let players choose to attack, block, or parry each turn.
- Add chance-based outcomes for parry.

---

## Level 7: Advanced Opponents & AI

**Objective:**  
Make battles more challenging with smarter enemies.

**Instructions:**
- Create enemy subclasses with unique stats, weapons, and behaviors.
- Implement simple AI: choose defensive moves or healing when appropriate.
- Add bosses with special abilities or multi-phase fights.

---

## Level 8: Battle Progression & Upgrades

**Objective:**  
Create a multi-battle system and progression.

**Instructions:**
- Add multiple rounds or enemies to defeat in sequence.
- Allow players to earn upgrades (stat boosts, new weapons) after victories.
- Track and display progress, victories, and defeats.

---

## Level 9: Game Saving, Victory, and Replayability

**Objective:**  
Allow progress saving, define win/loss conditions, and encourage replays.

**Instructions:**
- Implement save/load for player stats, inventory, and progress.
- Set clear victory conditions (e.g., defeat a final boss).
- Display win/loss messages and allow the user to restart the game.

---

## Level 10: Advanced Features (Optional)

**Objective:**  
Push creativity and OOP mastery.

**Instructions:**
- Add inventory management UI.
- Implement a shop for buying/selling items.
- Create multiplayer (local or online).
- Add random events, achievements, and story elements.

---

Each level builds on the previous one, introducing new OOP concepts and game design challenges. Progress through the levels for a robust, customizable battle game!