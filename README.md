# 🐍 Python Learning Journey

This repository documents my Python learning journey through project-based development and incremental software design improvements.

## Contents

- Basic Python syntax
- Variables
- Input and output
- If statements
- Loops
- list

## Goal

Learn Python and build real projects step by step.

This repository documents my Python learning process through small projects and continuous refactoring.

I focus on understanding programming through building real applications instead of memorizing syntax.

---

# 🎮 Current Project: Guess the Number Game

A terminal-based number guessing game built step by step while learning Python fundamentals, data structures, and software architecture concepts.


# ✨ Features

## Gameplay
- Random number generation (1–100)
- Difficulty selection
- Limited attempts system
- Replay system
- Guess feedback (Too high / Too low / Correct)


## Input System
- Input validation
- Exception handling (`try / except`)
- Range validation


## History System
- Structured guess history tracking
- List-based state management
- Dictionary-based history records

Example:

```python
{
    "guess": 42,
    "result": "correct"
}
```


## Presentation System
- Custom history viewer
- Result display abstraction
- Separate presentation functions


# 🧠 Key Python Concepts Practiced

## Core Python
- Variables
- Data types
- Input / output
- Conditional statements
- Loops
- Functions


## Error Handling
- `try`
- `except`
- Defensive input handling


## Data Structures

### List
- `append()`
- indexing
- negative indexing
- `len()`
- traversal with `for`

### Dictionary (dict)
- key/value structure
- structured records
- data access with `record["key"]`


# 🏗️ Software Design Concepts

## Layered Architecture

The project is separated into:

- Input Layer
- Logic Layer
- Presentation Layer
- Game Layer


## Separation of Concerns

### Logic Layer
Responsible for game logic only.

Example:

```python
return "high"
return "low"
return "correct"
```


### Presentation Layer
Responsible for displaying information to the user.

Example:

```python
show_result()
show_history()
```

## Structured Data Design

The project evolved from:

```python
history = [30, 50, 42]
```

to:

```python
history = [
    {"guess": 30, "result": "low"},
    {"guess": 50, "result": "high"}
]
```

This introduced:
- structured records
- program state tracking
- data traversal
- presentation abstraction


# 📈 Project Evolution

## Version 1
- Basic guessing game
- Simple loop logic


## Version 2
- Function-based structure
- Difficulty system
- Replay system
- Error handling


## Version 3 (Current)
- Structured history system
- List + dictionary architecture
- Logic/UI separation
- State-driven design
- Presentation abstraction
- Cleaned control flow


# 🚀 Planned Improvements

- Statistics system
- Multi-file project structure
- Save/load system
- Better terminal UI
- Data analysis features
- Modular architecture


# 🧭 Learning Philosophy

This project follows a project-driven learning approach:

> "Understand by building. Improve by refactoring."

The focus is on:
- understanding program structure
- thinking in systems
- designing maintainable code
- learning software architecture incrementally


# 📚 Current Learning Direction

Currently exploring:
- Python data structures
- structured data systems
- software architecture fundamentals
- state-driven programming
- clean code organization