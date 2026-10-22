# Deep-Dive Explanation: 09-majority-element-boyer-moore

## 💡 Algorithmic Thinking

The Boyer-Moore Voting Algorithm relies on canceling out dissimilar pairs:
- If a majority element occurs strictly more than $\lfloor n/2 \rfloor$ times, even if every other element cancels out one of its occurrences, the majority candidate will still survive with a positive count.
- At `count == 0`, we adopt the current number as the new candidate.
- Matching numbers increment `count`; different numbers decrement `count`.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(n)$ single linear scan.
- **Space Complexity**: $O(1)$ auxiliary space (only `candidate` and `count` variables).
