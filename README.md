# 🐍 Python Learning Journey

This repository documents my Python learning journey through project-based development, continuous refactoring, and software architecture exploration.

## Contents

### Python Fundamentals

* Variables
* Input and output
* Conditional statements
* Loops
* Functions

### Data Structures

* List
* Dictionary (dict)

### Software Design

* Layered architecture
* Separation of concerns
* State-driven design
* Refactoring

## Goal

Learn Python by building real projects and gradually developing software engineering skills.

Rather than memorizing syntax, I focus on understanding how programs are structured, how data flows through a system, and how code can be improved through iterative refactoring.



# 🎮 Current Project: Guess the Number Game

A terminal-based number guessing game that evolved from a simple script into a structured mini-application.

The project serves as a learning platform for Python fundamentals, data structures, software design, and project organization.


# ✨ Features

## Gameplay

* Random number generation (1–100)
* Difficulty selection
* Limited attempts system
* Replay system
* Guess feedback (Too High / Too Low / Correct)

## Input System

* Input validation
* Exception handling (`try / except`)
* Range validation

## History System

* Structured guess history tracking
* List-based storage
* Dictionary-based records

Example:

```python
{
    "guess": 42,
    "result": "correct"
}
```

## Statistics System

Tracks game outcomes:

```python
{
    "high": 3,
    "low": 2,
    "correct": 1
}
```

Provides simple gameplay analytics and state tracking.

## Game State System

The project introduces a centralized game state object:

```python
game_state = {
    "number": 42,
    "max_chance": 10,
    "history": [],
    "stats": {}
}
```

This reduces parameter passing and groups related game data into a single structure.


# 🧠 Key Python Concepts Practiced

## Core Python

* Variables
* Data types
* Input / output
* Conditional statements
* Loops
* Functions

## Error Handling

* `try`
* `except`
* Defensive input validation

## Data Structures

### List

* `append()`
* indexing
* negative indexing
* `len()`
* traversal with `for`

### Dictionary (dict)

* key/value pairs
* structured records
* nested dictionaries
* dictionary traversal
* state management


# 🏗️ Software Design Concepts

## Layered Architecture

The project is organized into:

* Input Layer
* Logic Layer
* Data Layer
* Presentation Layer
* Game Layer

## Separation of Concerns

### Logic Layer

Responsible for game rules and decision making.

Example:

```python
return "high"
return "low"
return "correct"
```

### Presentation Layer

Responsible for displaying information.

Example:

```python
show_result()
show_summary()
```

### Data Layer

Responsible for creating and managing game data structures.

Example:

```python
create_game_state()
```


## State-Driven Design

The project evolved from managing multiple independent variables:

```python
number
history
stats
max_chance
```

to a centralized state object:

```python
game_state
```

This approach improves maintainability and scalability while reducing parameter complexity.


# 📈 Project Evolution

## Version 1

* Basic guessing game
* Simple loop logic

## Version 2

* Function-based architecture
* Difficulty system
* Replay system
* Error handling

## Version 3

* Structured history system
* List + dictionary architecture
* Logic/UI separation

## Version 4 (Current)

* Statistics system
* Data Layer
* Game State architecture
* State-driven design
* Reduced parameter coupling
* Improved project structure


# 🚀 Planned Improvements

* Multi-file project structure
* Save/load system
* Best score tracking
* Session statistics
* Better terminal UI
* Persistent data storage


# 🧭 Learning Philosophy

This project follows a project-driven learning approach:

> "Understand by building. Improve by refactoring."

The focus is on:

* understanding program structure
* thinking in systems
* designing maintainable code
* learning software architecture incrementally


# 📚 Current Learning Direction

Currently exploring:

* Python data structures
* software architecture fundamentals
* state-driven programming
* code refactoring
* project organization
* clean code principles
