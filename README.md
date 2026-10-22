# Python Dojo 🥋

> **The Deliberate Practice Arena for Python Fluency, Algorithms, & Internals.**

Welcome to the **Python Dojo**. This repository is engineered for deliberate, rigorous mastery of Python's most foundational and frequently misunderstood concepts.

Rather than memorizing syntax or relying on high-level standard library shortcuts, this curriculum builds deep intuition by taking you under the hood of:
- **Recursion & Call Stacks**
- **Big O Complexity & Growth Analysis**
- **Hashing & Hash Maps from Scratch**
- **Closures & Decorators**

---

## 🗺️ Curriculum Roadmap

| Module | Topic | Core Focus | Drills |
| :--- | :--- | :--- | :--- |
| **`01-recursion`** | Recursion & The Call Stack | Base cases, frames, tree recursion, backtracking, memoization | 20 Drills |
| **`02-big-o-complexity`** | Algorithmic Complexity | Time & auxiliary space, loop growth, amortized cost, trade-offs | 20 Drills |
| **`03-hashing-and-hashmaps`** | Hash Maps Under the Hood | Hash functions, modulo slots, separate chaining, collision handling | 20 Drills |
| **`04-decorators-and-closures`** | Decorators & Closures | First-class functions, decoration time vs call time, wrappers, state | 20 Drills |
| **`05-elite-challenge-arena`** | The Boss Assessment | The complete 100-mark test covering all four pillars under exam constraints | Capstone |

---

## 🥋 How to Train

Every drill across every module is organized for deliberate practice:

```text
module-name/
├── README.md                      <-- Deep conceptual guide & mental models
├── drills/
│   └── 01-drill-name/
│       ├── README.md              <-- Problem statement, constraints & examples
│       ├── exercise.py            <-- Starter stub (write your solution here)
│       └── test_exercise.py       <-- Rigorous test suite (unit tests & edge cases)
└── solutions/
    └── 01-drill-name/
        ├── solution.py            <-- Pedagogical, fully commented solution
        └── explanation.md         <-- Deep dive into time, space & alternate approaches
```

### 3-Step Training Workflow:

1. **Read & Trace**: Read the drill's `README.md`. Trace your logic on paper or in comments before writing code.
2. **Implement**: Open `exercise.py` and write your implementation. Do not use forbidden shortcuts!
3. **Verify with Tests**: Run the unit test suite:
   ```bash
   python test_exercise.py
   ```
   When all tests pass, check your solution against the master guide in `solutions/` to compare style, time complexity, and edge case resilience.

---

## ⚡ The Dojo Golden Rules
1. **No Magic**: When a drill asks you to implement a data structure or algorithm, standard library cheats (`dict`, `set`, `sum()`, `sorted()`) are strictly forbidden.
2. **Edge Cases First**: Always account for zero, negative numbers, empty collections, single elements, and large inputs.
3. **Trace Before Running**: If you cannot trace where a return value goes in the call stack, do not guess—draw the stack frames.
