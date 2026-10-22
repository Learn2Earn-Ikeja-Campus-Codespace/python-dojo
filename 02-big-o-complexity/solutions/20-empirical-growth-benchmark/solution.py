"""
Solution for Drill 20: Empirical Growth Rate Benchmark Harness
Module: 02-big-o-complexity
"""
import time


def measure_growth_ratio(fn, n1: int, n2: int) -> float:
    """Measures the execution time ratio T(n2) / T(n1) for the given function."""
    input1 = list(range(n1))
    input2 = list(range(n2))

    # Warm up CPU caches
    fn(input1[:100])

    def time_it(data, reps=3):
        start = time.perf_counter()
        for _ in range(reps):
            fn(data)
        return (time.perf_counter() - start) / reps

    t1 = time_it(input1)
    t2 = time_it(input2)

    return t2 / max(t1, 1e-9)
