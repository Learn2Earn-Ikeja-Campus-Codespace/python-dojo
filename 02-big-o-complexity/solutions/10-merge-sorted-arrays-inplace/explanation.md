# Deep-Dive Explanation: 10-merge-sorted-arrays-inplace

## 💡 Algorithmic Thinking

Merging from left-to-right would overwrite elements in `nums1` that haven't been processed yet, necessitating an extra array ($O(m)$ space).
By merging **backwards from the end** (`p = m + n - 1`):
- The empty slots are at the end of `nums1`.
- The largest available element (comparing `nums1[p1]` vs `nums2[p2]`) is placed directly at `nums1[p]`.
- Existing unread elements in `nums1` are never prematurely overwritten.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(m + n)$
- **Space Complexity**: $O(1)$ auxiliary space.
