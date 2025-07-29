# Roadmap: Learning Object-Oriented Programming (OOP) in Python

This roadmap guides you from foundational OOP concepts to building a terminal-based fighting game. Each lesson integrates theory with hands-on coding, and the capstone project is scaffolded throughout so you apply new skills as you learn.

---

## OOP Lessons Roadmap

### 1. **Getting Started: Classes and Objects**
   - What are classes and objects?
   - Defining classes, attributes, and methods
   - The `__init__` constructor
   - Creating and using instances
   - **Project Step:** Create a basic Fighter class

### 2. **Encapsulation & Information Hiding**
   - The concept of encapsulation (one of the four pillars)
   - Public, protected, and private attributes (Python conventions)
   - Property decorators (`@property`) and getter/setter methods
   - **Project Step:** Add stats (health, power) and encapsulate them in Fighter

### 3. **Inheritance and Code Reuse**
   - The concept of inheritance (pillar two)
   - Building class hierarchies and using `super()`
   - Method overriding
   - **Project Step:** Create subclasses (e.g., Mage, Warrior) that inherit from Fighter

### 4. **Polymorphism & Duck Typing**
   - The concept of polymorphism (pillar three)
   - Method overriding and dynamic behavior
   - Special (“dunder”) methods (`__str__`, `__repr__`, etc.)
   - Duck typing and Python’s flexible approach
   - **Project Step:** Implement polymorphic attack methods for subclasses

### 5. **Abstraction & Interfaces**
   - The concept of abstraction (pillar four)
   - Using abstract base classes (ABC) for common interfaces
   - Designing for abstraction and future extensibility
   - **Project Step:** Plan out a Move system using abstraction

### 6. **Composition & Relationships**
   - "Has-a" relationships vs. "is-a" relationships
   - Composing objects (e.g., Fighter has Moves/Inventory)
   - Collaborating classes and code organization
   - **Project Step:** Implement Moves, Inventory, and GameEngine classes

### 7. **Modern Python OOP Tools**
   - Dataclasses (`@dataclass`) for cleaner class definitions
   - Type hints and static analysis
   - Mixins and multiple inheritance
   - Code organization tips for larger projects
   - **Project Step:** Refactor classes with dataclasses and type hints

### 8. **Capstone: Terminal-Based Fighting Game**
   - Integrate all classes and game logic
   - Handle user input and battle mechanics
   - Playtesting, refactoring, and debugging
   - **Final Project:** Complete your terminal-based fighting game!

---

## Practice Integration

- **Mini-Projects & Checkpoints:**  
  After each lesson, enhance your fighting game with the new concept.  
  Example: After inheritance, add unique abilities for each fighter subclass.

- **Code Review & Refactoring:**  
  Regularly review and improve your code based on new OOP knowledge.

---

## Optional & Independent Exploration

- Design patterns (Singleton, Factory, Observer)
- Testing OOP code (`unittest`, `pytest`)
- UML diagrams for class relationships
- Comparing Python's OOP with other languages

---

**By following this roadmap, you'll master OOP in Python and build a complete, playable fighting game!**