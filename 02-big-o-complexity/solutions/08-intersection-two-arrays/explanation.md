# Deep-Dive Explanation: 08-intersection-two-arrays

## 💡 Algorithmic Thinking

A nested loop checks every element of `a` against `b` in $O(|a| \cdot |b|)$ time.
Converting the smaller list (or list `b`) into a hash set takes $O(|b|)$ time.
Scanning `a` takes $O(|a|)$ checks, each executing in $O(1)$ time.
Tracking already-appended elements in `seen` ensures each duplicate is reported only once.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(|a| + |b|)$
- **Space Complexity**: $O(|b| + \min(|a|, |b|))$
