# Explanation: 18-tower-of-hanoi

## Divide and Conquer Disk Transfers
The solution to $n$ disks requires solving $n-1$ twice plus 1 move for the base disk:
$$T(n) = 2T(n-1) + 1 = 2^n - 1$$
