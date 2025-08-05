# Progressive OOP Card Game Assignments

This sequence of assignments will guide you in building a card game (like "War" or "Blackjack") using Object-Oriented Programming in Python. Each level increases the challenge, introducing more advanced OOP concepts and game mechanics.

---

## Level 1: Deck and Card Basics

**Objective:**  
Implement the fundamental classes for a deck of cards.

**Instructions:**
- Create a `Card` class with attributes: `suit`, `rank`, and optionally `value`.
- Create a `Deck` class that can generate a standard 52-card deck.
- Implement methods to shuffle the deck and deal a card.
- Print the deck before and after shuffling.

---

## Level 2: Simple Two-Player Game

**Objective:**  
Simulate a basic two-player card game (e.g., "War").

**Instructions:**
- Create a `Player` class with a hand (list of cards).
- Deal half the deck to each player.
- Each round, both players play the top card; higher card wins the round.
- Track and print the winner of each round and the overall winner.

**Stretch:**  
Add the ability to replay the game.

---

## Level 3: Game Logic and Rounds

**Objective:**  
Add a game loop and round tracking.

**Instructions:**
- Implement a loop to play rounds until one player runs out of cards.
- Track the number of rounds and print a summary at the end.
- Handle ties appropriately.

**Stretch:**  
Add a scoring system.

---

## Level 4: User Interaction

**Objective:**  
Allow a human to play against the computer.

**Instructions:**
- Let the user choose to play a card or pass each round.
- Print hands and round results clearly.
- Computer plays automatically.

**Stretch:**  
Allow the user to name their player.

---

## Level 5: Advanced Card Effects

**Objective:**  
Add special cards or effects.

**Instructions:**
- Add cards with special effects (e.g., "Draw Two", "Skip Turn").
- Handle these effects in the game loop.
- Update the `Card` and `Game` classes to support these features.

**Stretch:**  
Create subclasses for different card types.

---

## Level 6: Multiple Players

**Objective:**  
Support more than two players.

**Instructions:**
- Update the game logic to handle 3 or more players.
- Handle rounds and scoring appropriately.
- Print a leaderboard after each round.

**Stretch:**  
Allow for elimination when a player runs out of cards.

---

## Level 7: Game Variants

**Objective:**  
Implement multiple game rules (e.g., "War", "Blackjack", "Go Fish").

**Instructions:**
- Use inheritance to create different game types.
- Allow the user to choose a variant at the start.
- Implement distinct logic for each variant.

**Stretch:**  
Add instructions and help messages for each game type.

---

## Level 8: Saving, Loading, and Replayability

**Objective:**  
Allow players to save and load game progress.

**Instructions:**
- Serialize the game state (deck, players, hands, scores).
- Implement save/load functions.
- Allow users to restart or resume a game.

**Stretch:**  
Track statistics (games played, win/loss record).

---

## Level 9: Advanced Features (Optional)

**Objective:**  
Challenge yourself with creative extensions.

**Instructions:**
- Add a shop or upgrades for players.
- Implement a graphical or web interface.
- Support multiplayer over the network.
- Add achievements and unlockables.

---

Progress through these levels to master OOP and build a robust, replayable card game!