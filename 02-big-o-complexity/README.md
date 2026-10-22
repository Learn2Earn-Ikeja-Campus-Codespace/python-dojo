# Module 02: Big O Complexity & Algorithmic Growth ⏱️

> *"Big O does not measure stopwatch seconds; it measures how resource demands grow as input size scales towards infinity."*

Understanding Big O is what separates someone who merely writes code that passes from someone who can architect scalable, production-grade software. In this module, you will master **time complexity**, **auxiliary space complexity**, **amortized analysis**, and the real-world **trade-offs** between CPU cycles, RAM, and data structures.

---

## 🧠 The Core Mental Models

### 1. Growth Rate Over Constants
If Algorithm A takes $100n$ operations and Algorithm B takes $n^2$ operations:
* For $n = 10$: Algorithm A takes 1,000 steps; Algorithm B takes 100 steps. (B looks faster!)
* For $n = 10,000$: Algorithm A takes 1,000,000 steps; Algorithm B takes 100,000,000 steps. (A crushes B!)

Big O drops constant factors ($O(2n) \to O(n)$) and lower-order terms ($O(n^2 + 5n) \to O(n^2)$) because as $n \to \infty$, the highest-order term dictates scalability.

---

### 2. Time vs. Auxiliary Space Complexity
- **Time Complexity**: How the number of fundamental operations grows with input size $n$.
- **Auxiliary Space Complexity**: How much **extra memory** the algorithm allocates beyond the input itself.
  - Slicing a list (`nums[1:]`) allocates $O(n)$ extra memory per slice.
  - An index pointer (`index += 1`) uses $O(1)$ auxiliary memory.
  - Recursion depth of $k$ frames costs $O(k)$ auxiliary stack space.

---

### 3. The Big O Hierarchy (From Best to Worst)

| Notation | Name | Practical Example | $n = 1,000,000$ operations |
| :--- | :--- | :--- | :--- |
| **$O(1)$** | Constant | Hash map lookup, list index access | 1 step |
| **$O(\log n)$** | Logarithmic | Binary search, binary heap operations | $\approx 20$ steps |
| **$O(n)$** | Linear | Single loop, linear search, list copy | 1,000,000 steps |
| **$O(n \log n)$** | Linearithmic | Merge sort, Timsort (`sorted()`), heap sort | $\approx 20,000,000$ steps |
| **$O(n^2)$** | Quadratic | Nested loops, bubble sort, naive duplicate check | $1,000,000,000,000$ steps (Freezes!) |
| **$O(2^n)$** | Exponential | Naive recursive Fibonacci, power set | Impossible for large $n$ |
| **$O(n!)$** | Factorial | Generating all permutations | Fails even for $n = 20$ |

---

### 4. The Classic Fallacies to Avoid
1. **"Using a set makes my function $O(1)$"**:
   - Checking an item in a set is expected $O(1)$.
   - But building a set from $n$ items costs $O(n)$ time and $O(n)$ space!
   - Checking $n$ items against a set inside a loop is $n \times O(1) = O(n)$ total time.
2. **"Big O is exact execution time"**:
   - Hardware, CPU cache locality, branch prediction, and Python interpreter overhead affect real seconds. Big O predicts the **scaling curve**, not the millisecond timer.
3. **Worst vs. Average vs. Best Case**:
   - Linear search best case: $O(1)$ (target is at index 0).
   - Linear search worst case: $O(n)$ (target is at the end or absent).

---

## 🗺️ Module 02 Drill Directory (20 Progressive Drills)

### Level 1: Foundations & Growth Rate Analysis (Drills 01 – 06)
* **01-has-duplicate-tradeoffs**: The 3 implementations of duplicate checking ($O(n^2)$ vs $O(n)$ space vs $O(n \log n)$ sorting).
* **02-constant-vs-linear**: Operations counting in $O(1)$ vs $O(n)$ sequences.
* **03-nested-loop-counting**: Analyzing dependent nested loops ($\sum_{i=1}^n i = \frac{n(n-1)}{2} = O(n^2)$).
* **04-logarithmic-growth**: Step-halving loops and integer divisions ($O(\log n)$).
* **05-space-complexity-audit**: Distinguishing in-place pointer mutation $O(1)$ from allocations $O(n)$.
* **06-prefix-sum-optimization**: Replacing an $O(n^2)$ repeated slice sum with an $O(1)$ query prefix sum.

### Level 2: Algorithmic Trade-offs & Common Bottlenecks (Drills 07 – 13)
* **07-two-sum-tradeoffs**: Compare brute-force $O(n^2)$ vs hash map $O(n)$ time/$O(n)$ space vs two-pointer $O(n \log n)$ time/$O(1)$ space.
* **08-intersection-two-arrays**: Optimize finding common elements across two lists of sizes $M$ and $N$.
* **09-majority-element-boyer-moore**: Upgrade frequency counting from $O(n)$ space down to Boyer-Moore $O(1)$ auxiliary space.
* **10-merge-sorted-arrays-inplace**: In-place merge without allocating a new output array ($O(1)$ space).
* **11-moving-average-sliding-window**: Calculate window average in $O(1)$ per step instead of $O(k)$ recomputation.
* **12-matrix-search-elimination**: Search a sorted 2D matrix in $O(m + n)$ by pruning rows/columns from top-right.
* **13-find-missing-math-vs-set**: Compare set difference $O(n)$ space vs Gauss formula $\frac{n(n+1)}{2}$ $O(1)$ space.

### Level 3: Amortized Analysis & Benchmark-Grade Optimization (Drills 14 – 20)
* **14-amortized-array-growth**: Simulate dynamic array resizing and prove why append is amortized $O(1)$.
* **15-queue-via-two-stacks**: Implement FIFO queue using two LIFO stacks with amortized $O(1)$ dequeue.
* **16-longest-consecutive-sequence**: Find longest consecutive integers in $O(n)$ time using set intelligent skips.
* **17-product-except-self**: Compute array products without division in $O(n)$ time and $O(1)$ auxiliary space.
* **18-trapping-rainwater**: Compute elevation water trapping: compare brute force $O(n^2)$ to two-pointer $O(n)$ time and $O(1)$ space.
* **19-subarrays-with-k-sum**: Count subarrays summing to $k$ in $O(n)$ time using running prefix sum hash map.
* **20-benchmark-suite-timer**: Build an automated empirical benchmark runner measuring growth rate curve across input scales.
