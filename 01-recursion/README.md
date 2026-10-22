# Module 01: Recursion & The Call Stack 🔄

> *"To understand recursion, one must first understand recursion."*

Recursion is not magic—it is simply a function that calls itself to solve a smaller instance of the same problem. To master recursion, you must develop a clear mental model of the **call stack**.

---

## 🧠 The Mental Model: How Recursion Actually Works

### 1. Functions are Frames on a Stack
Every time any function is called in Python:
1. Python creates a **stack frame** in memory.
2. The stack frame holds the function's local variables, arguments, and the exact line of code where it is currently executing.
3. When function `A` calls function `B`, function `A` is **paused** and waits.
4. Function `B` runs to completion and produces a `return` value.
5. Function `B`'s stack frame is destroyed (popped off the stack), and function `A` resumes with `B`'s return value.

### 2. The Two Essential Laws of Recursion
Every working recursive function must have:
1. **The Base Case (Stopping Condition)**: The smallest, simplest input for which the answer is immediately known without further recursion (e.g. $n = 0$, an empty list `[]`, or a leaf node). Without this, the function recurses forever until Python halts with `RecursionError: maximum recursion depth exceeded`.
2. **The Recursive Step (Progress Toward Base Case)**: The call to itself with an input that is strictly closer to the base case (e.g. $n - 1$, or `lst[1:]`). If the input does not shrink or change, you enter an infinite loop.

---

## 🔍 Tracing an Execution: Follow the Return Values

Consider the classic summation of integers $1$ through $n$:

```python
def total(n: int) -> int:
    if n <= 0:
        return 0
    return n + total(n - 1)
```

If we call `total(4)`, here is the exact step-by-step lifecycle:

```text
WINDING PHASE (Stack Grows Upward):
[Frame 4] total(4) calls total(3) and waits...
  [Frame 3] total(3) calls total(2) and waits...
    [Frame 2] total(2) calls total(1) and waits...
      [Frame 1] total(1) calls total(0) and waits...
        [Frame 0] total(0) hits base case -> returns 0!

UNWINDING PHASE (Stack Collapses Downward):
      [Frame 1] total(1) resumes: 1 + 0 = 1 -> returns 1
    [Frame 2] total(2) resumes: 2 + 1 = 3 -> returns 3
  [Frame 3] total(3) resumes: 3 + 3 = 6 -> returns 6
[Frame 4] total(4) resumes: 4 + 6 = 10 -> returns 10
```

Notice two critical insights:
1. **Work happens on the way down or on the way up**: In this example, the addition `n + ...` happens during the **unwinding phase** as values travel back up.
2. **Space complexity is $O(n)$**: Even though we didn't create a list, the computer allocated $n + 1$ stack frames in memory!

---

## 🗺️ Module 01 Drill Directory (20 Progressive Drills)

The 20 drills are ordered by conceptual difficulty:

### Level 1: Foundations & The Linear Call Stack (Drills 01 – 06)
* **01-countdown-sum**: Sum odd positive integers down from $n$ to 1 (Quest 1 from Challenge).
* **02-factorial-safe**: Implement factorial with strict validation for negatives and types.
* **03-recursive-string-reverse**: Reverse a string purely by decomposing head and tail.
* **04-sum-list-pure**: Recursively sum a list without `sum()`, slicing index pointers instead.
* **05-count-occurrences**: Count occurrences of a target item in a list recursively.
* **06-palindrome-check**: Determine if a word is a palindrome by comparing extremities.

### Level 2: Tree Recursion & Structural Decomposition (Drills 07 – 13)
* **07-fibonacci-memo**: Compare naive tree recursion $O(2^n)$ vs memoized $O(n)$.
* **08-binary-search**: Recursive divide-and-conquer on a sorted array with pointer tracking.
* **09-flatten-nested-list**: Flatten an arbitrarily deeply nested list of lists.
* **10-nested-dict-lookup**: Find a nested key in a dictionary of arbitrary depth.
* **11-power-function**: Fast exponentiation in $O(\log n)$ using $x^n = (x^{n/2})^2$.
* **12-greatest-common-divisor**: Euclidean algorithm via pure recursion.
* **13-pascal-triangle-cell**: Calculate value at row $r$, col $c$ of Pascal's triangle recursively.

### Level 3: Combinatorics & Backtracking (Drills 14 – 20)
* **14-generate-subsets**: Generate all power sets of a collection via include/exclude decisions.
* **15-string-permutations**: Generate all unique permutations of a string.
* **16-climbing-stairs**: Count ways to climb $n$ stairs with steps of 1, 2, or 3.
* **17-coin-change-count**: Count distinct ways to make change for amount $N$ with given coin denominations.
* **18-tower-of-hanoi**: Generate the optimal sequence of moves to transfer disks.
* **19-nested-json-key-counter**: Traverse and count keys matching a pattern in nested JSON structures.
* **20-maze-pathfinder**: Backtracking pathfinder through a 2D grid from start to finish.
