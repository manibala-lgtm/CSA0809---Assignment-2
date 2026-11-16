"""
Q1 - Decisions with Many Boundaries
Run: python q1_decisions.py
"""

households = [
    ("H1", 100, False, False),
    ("H2", 100, True, False),
    ("H3", 101, False, False),
    ("H4", 101, True, False),
    ("H5", 200, True, False),
    ("H6", 201, True, False),
    ("H7", 250, False, True),
    ("H8", 250, True, False),
]

def separate_if_buggy(units, ration_card, elderly_over_80):
    """Intentionally flawed: the second condition overlaps the first."""
    decisions = []
    if units <= 100:
        decisions.append("FULL subsidy")
    # BUG: this should start at 101, not include all values <= 200.
    if units <= 200 and ration_card:
        decisions.append("PARTIAL subsidy")
    if units > 200 and elderly_over_80:
        decisions.append("SPECIAL subsidy")
    if units > 200 and not elderly_over_80:
        decisions.append("NO subsidy")
    return decisions or ["NO subsidy"]


def decide_if_elif(units, ration_card, elderly_over_80):
    if units <= 100:
        return "FULL subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "PARTIAL subsidy"
        else:
            return "NO subsidy"
    elif units > 200:
        if elderly_over_80:
            return "SPECIAL subsidy"
        else:
            return "NO subsidy"


def decide_boolean(units, ration_card, elderly_over_80):
    if units <= 100:
        return "FULL subsidy"
    elif 101 <= units <= 200 and ration_card:
        return "PARTIAL subsidy"
    elif units > 200 and elderly_over_80:
        return "SPECIAL subsidy"
    else:
        return "NO subsidy"


def match_case_decision(units, ration_card, elderly_over_80):
    # Python 3.10+
    match units:
        case value if value <= 100:
            return "FULL subsidy"
        case value if 101 <= value <= 200 and ration_card:
            return "PARTIAL subsidy"
        case value if value > 200 and elderly_over_80:
            return "SPECIAL subsidy"
        case _:
            return "NO subsidy"


def lookup_decision(units, ration_card, elderly_over_80):
    # Ordered upper-limit slabs; conditions depending on card/age are checked
    # after the matching slab is found.
    slabs = [(100, "LOW"), (200, "MIDDLE"), (float("inf"), "HIGH")]
    for upper_limit, slab in slabs:
        if units <= upper_limit:
            if slab == "LOW":
                return "FULL subsidy"
            if slab == "MIDDLE":
                return "PARTIAL subsidy" if ration_card else "NO subsidy"
            return "SPECIAL subsidy" if elderly_over_80 else "NO subsidy"


def main():
    print("PREDICTIONS / TEST DATA")
    print("ID  Units  Ration  Age>80  Expected decision")
    for hid, units, ration, elderly in households:
        print(f"{hid:3} {units:6}  {str(ration):6}  {str(elderly):6}  "
              f"{decide_if_elif(units, ration, elderly)}")

    print("\nCOMPARISON")
    for hid, units, ration, elderly in households:
        buggy = separate_if_buggy(units, ration, elderly)
        correct = decide_if_elif(units, ration, elderly)
        print(f"{hid}: separate-if={buggy} | if-elif-else={correct}")

    print("\nALTERNATIVE METHODS")
    print("match-case:", match_case_decision(200, True, False))
    print("lookup loop:", lookup_decision(201, False, True))

    print("\nCOMPLEXITY")
    print("if-elif-else: O(1) time for this fixed number of rules; O(1) space.")
    print("match-case with guards: O(k) worst case for k sequential cases; O(1) space.")
    print("lookup list: O(k) worst-case search for k slabs; O(k) slab storage.")
    print("Nested if is useful when a decision has a clear second-stage check.")
    print("Combined Boolean conditions are compact for short, independent rules.")


if __name__ == "__main__":
    main()
