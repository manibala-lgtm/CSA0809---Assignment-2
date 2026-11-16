"""
Q6 - Recursion and Its Limits
Run: python q6_recursion.py
"""

from functools import lru_cache
import sys
import time

naive_calls = 0
memo_calls = 0


def ways_naive(n):
    """Plain recursion: number of ways to climb n steps using 1 or 2 steps."""
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    """Memoised recursion."""
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    # Completed TODO 1: recursive calls must call ways_memo, not ways_naive.
    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_loop(n):
    """Iterative version retaining only the previous two results."""
    if n <= 1:
        return 1
    previous_two, previous_one = 1, 1
    for _ in range(2, n + 1):
        previous_two, previous_one = previous_one, previous_two + previous_one
    return previous_one


def main():
    print("ANSWERS FOR n = 1 TO 6")
    for n in range(1, 7):
        print(f"n={n}: {ways_loop(n)}")

    print("\nCALL TREE FOR n=5 (repeated branches shown)")
    print("ways(5)")
    print("├─ ways(4)")
    print("│  ├─ ways(3)")
    print("│  │  ├─ ways(2)")
    print("│  │  └─ ways(1)")
    print("│  └─ ways(2)  [recomputed]")
    print("└─ ways(3)  [recomputed]")

    print("\nNAIVE VS MEMOISED CALL COUNTS")
    for n in (10, 20, 25, 30):
        naive_calls = 0
        start = time.perf_counter()
        naive_result = ways_naive(n)
        naive_time = time.perf_counter() - start
        naive_count = naive_calls

        ways_memo.cache_clear()
        memo_calls = 0
        start = time.perf_counter()
        memo_result = ways_memo(n)
        memo_time = time.perf_counter() - start
        memo_count = memo_calls

        print(
            f"n={n}: same={naive_result == memo_result}, "
            f"naive calls={naive_count:,}, memo calls={memo_count:,}, "
            f"naive time={naive_time:.6f}s, memo time={memo_time:.6f}s"
        )

    print("\nTEST n=1000")
    print("Current recursion limit:", sys.getrecursionlimit())
    ways_memo.cache_clear()
    try:
        print("Memoised recursive result:", ways_memo(1000))
    except RecursionError as error:
        print("RecursionError caught:", error)
        print("Memoisation avoids repeated work, but recursion still uses a deep call stack.")

    start = time.perf_counter()
    loop_result = ways_loop(1000)
    loop_time = time.perf_counter() - start
    print("Loop result for n=1000:", loop_result)
    print(f"Loop time for n=1000: {loop_time:.6f}s")

    print("\nCOMPLEXITY")
    print("Plain recursion: exponential time O(2^n), O(n) stack space.")
    print("Memoised recursion: O(n) time, O(n) cache and O(n) stack space.")
    print("Loop: O(n) time and O(1) auxiliary space.")
    print("Deployment decision: use the loop for n up to 1000; it avoids recursion-depth risk.")
    print("Raising the recursion limit is not the preferred fix for a problem with a simple loop solution.")


if __name__ == "__main__":
    main()
