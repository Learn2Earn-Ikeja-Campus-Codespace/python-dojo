# Drill 15: Queue via Two Stacks (Amortized $O(1)$)

## Learning Target
Implement a FIFO Queue using two LIFO stacks (`in_stack`, `out_stack`). Prove that while a single `dequeue` might take $O(n)$ when transferring elements, each element is moved at most twice, making operations **amortized $O(1)$**.

---

## Problem Statement

Implement `QueueViaStacks`:
- `enqueue(val)`: Pushes element onto queue in $O(1)$ time.
- `dequeue()`: Removes and returns element from front in amortized $O(1)$ time.
- `peek()`: Returns front element without removing.
- `empty() -> bool`: Returns `True` if queue has no elements.

Raises `IndexError` on dequeue/peek of empty queue.

---

## Examples

```python
q = QueueViaStacks()
q.enqueue(1)
q.enqueue(2)
q.peek()     # 1
q.dequeue()  # 1
q.dequeue()  # 2
q.empty()    # True
```
