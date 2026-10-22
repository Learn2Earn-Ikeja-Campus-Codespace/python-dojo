# Deep-Dive Explanation: 15-queue-via-two-stacks

## 💡 Algorithmic Thinking

Two stacks reverse the LIFO order twice, restoring FIFO order:
- `enqueue()` pushes directly onto `_in_stack` in $O(1)$.
- `dequeue()` and `peek()` draw from `_out_stack`.
- When `_out_stack` is empty, all elements from `_in_stack` are popped and pushed into `_out_stack`.
Each element enters `_in_stack` once, moves to `_out_stack` once, and leaves `_out_stack` once (3 operations total). Hence, amortized cost per operation is $O(1)$.

---

## 📊 Complexity Analysis

- **Enqueue Time**: $O(1)$
- **Dequeue / Peek Time**: Amortized $O(1)$ (Worst-case single call $O(n)$)
- **Space Complexity**: $O(n)$ to store $n$ queued items.
