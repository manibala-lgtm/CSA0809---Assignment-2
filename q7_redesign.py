"""
Q7 - Diagnose, Redesign and Validate
Selected program: Q6 naive recursive stair-counting.
Redesign: memoisation avoids recomputing the same subproblems.
Run: python q7_redesign.py
"""

from functools import lru_cache
import time

original_calls = 0
redesigned_calls = 0


def original_ways(n):
    global original_calls
    original_calls += 1
    if n <= 1:
        return 1
    return original_ways(n - 1) + original_ways(n - 2)


@lru_cache(maxsize=None)
def redesigned_ways(n):
    global redesigned_calls
    redesigned_calls += 1
    if n <= 1:
        return 1
    return redesigned_ways(n - 1) + redesigned_ways(n - 2)


def timed_call(function, n):
    start = time.perf_counter()
    result = function(n)
    elapsed = time.perf_counter() - start
    return result, elapsed


def main():
    print("Q7 DESIGN CHALLENGE: ORIGINAL VS REDESIGNED")
    print("Diagnosis: plain recursion calculates the same ways(n) subproblems repeatedly.")
    print("Objective: produce the same answer with substantially fewer function calls.")
    print("Redesign: cache each computed ways(n) result and reuse it.")
    print("Trade-off: the cache requires O(n) extra memory.")

    for n in (20, 25, 30):
        original_calls = 0
        original_result, original_time = timed_call(original_ways, n)
        original_count = original_calls

        redesigned_ways.cache_clear()
        redesigned_calls = 0
        redesigned_result, redesigned_time = timed_call(redesigned_ways, n)
        redesigned_count = redesigned_calls

        print(f"\nn={n}")
        print("Same result:", original_result == redesigned_result)
        print(f"Original:   calls={original_count:,}, time={original_time:.6f}s")
        print(f"Redesigned: calls={redesigned_count:,}, time={redesigned_time:.6f}s")
        if redesigned_count:
            print(f"Call reduction: {original_count / redesigned_count:.2f} times fewer calls")

    print("\nPSEUDOCODE")
    print("ways(n):")
    print("    if n <= 1: return 1")
    print("    if n is already cached: return cached value")
    print("    answer = ways(n-1) + ways(n-2)")
    print("    store answer in cache")
    print("    return answer")

    print("\nEVALUATION")
    print("Prediction: memoisation will keep the same result and reduce repeated calls.")
    print("Plain recursion: exponential time O(2^n), O(n) stack space.")
    print("Memoised recursion: O(n) time, O(n) cache plus O(n) stack.")
    print("The objective is achieved if the result matches and the measured call count falls.")
    print("For very deep inputs, an iterative O(n)-time, O(1)-space solution is safer.")
    print("The original is simpler for tiny n when performance is not important.")


if __name__ == "__main__":
    main()
