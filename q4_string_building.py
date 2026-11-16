"""
Q4 - Building Long Text: +=, join(), and f-string lines
Run: python q4_string_building.py
The program performs three timing rounds for each requested input size.
"""

import time


def build_plus(parts):
    text = ""
    for part in parts:
        text += part + ","
    return text


def build_join(parts):
    # Completed TODO 1: one join call; trailing comma matches build_plus.
    return ",".join(parts) + ("," if parts else "")


def build_fstring(parts):
    # Each line/item is formatted with an f-string, then joined once.
    formatted_parts = [f"{part}" for part in parts]
    return ",".join(formatted_parts) + ("," if formatted_parts else "")


def average_time(function, data, repeats=3):
    durations = []
    result = None
    for _ in range(repeats):
        start = time.perf_counter()
        result = function(data)
        durations.append(time.perf_counter() - start)
    return result, sum(durations) / len(durations), durations


def main():
    for size in (1_000, 10_000, 200_000):
        items = [f"Item{i}: Rs{i % 50}" for i in range(size)]

        plus_text, plus_avg, plus_runs = average_time(build_plus, items)
        join_text, join_avg, join_runs = average_time(build_join, items)
        f_text, f_avg, f_runs = average_time(build_fstring, items)

        print(f"\nLINES: {size:,}")
        print("Same output:", plus_text == join_text == f_text)
        print("Output length:", len(join_text))
        print(f"+= average:   {plus_avg:.6f} s | runs={ [round(x, 6) for x in plus_runs] }")
        print(f"join average: {join_avg:.6f} s | runs={ [round(x, 6) for x in join_runs] }")
        print(f"f-string avg: {f_avg:.6f} s | runs={ [round(x, 6) for x in f_runs] }")

    print("\nALTERNATIVE CONCEPTS")
    print("File writing: open a text file and write each part as it is produced.")
    print("StringIO: write parts to an in-memory stream, then call getvalue().")
    print("join: O(N) time in total output characters and O(N) memory for final output.")
    print("Repeated += can require repeated copying, up to O(N^2) total work in the general case.")
    print("File streaming uses small working memory; StringIO uses memory for the accumulated text.")
    print("CPython may optimise some += cases, but join is predictable and concise for many fragments.")


if __name__ == "__main__":
    main()
