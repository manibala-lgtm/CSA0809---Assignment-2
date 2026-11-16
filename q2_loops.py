"""
Q2 - Loops that Count Attempts
Run: python q2_loops.py
This is a classroom simulation; it does not connect to a real bank or account.
"""

CORRECT_OTP = "482913"


def verify_with_while(entries, max_attempts=3):
    print("\nWHILE LOOP")
    attempts = 0
    locked = False
    position = 0

    while attempts < max_attempts:
        if position >= len(entries):
            print("No more test entries supplied.")
            break

        entry = entries[position]
        position += 1

        if entry.strip() == "":
            print("Blank entry: not counted.")
            continue

        attempts += 1
        print(f"Attempt {attempts}: {entry}")

        # pass is a no-operation placeholder for an optional audit step.
        if entry == "AUDIT":
            pass

        if entry == CORRECT_OTP:
            print("OTP verified.")
            break
        print("Incorrect OTP.")

    else:
        locked = True
        print("Three counted attempts used. Account locked for 30 minutes.")

    return not locked


def verify_with_for(entries, max_attempts=3):
    print("\nFOR LOOP WITH range(max_attempts)")
    iterator = iter(entries)
    locked = False

    for attempt_number in range(1, max_attempts + 1):
        # Keep asking for an entry until a nonblank one is received.
        while True:
            try:
                entry = next(iterator)
            except StopIteration:
                print("No more test entries supplied.")
                return False

            if entry.strip() == "":
                print("Blank entry: not counted.")
                continue
            break

        print(f"Attempt {attempt_number}: {entry}")
        if entry == CORRECT_OTP:
            print("OTP verified.")
            break
        print("Incorrect OTP.")
    else:
        locked = True
        print("Three counted attempts used. Account locked for 30 minutes.")

    return not locked


def verify_with_security_question(entries, security_answer, correct_security_answer):
    extra_attempts = 2 if security_answer.strip().lower() == correct_security_answer.lower() else 0
    allowed = 3 + extra_attempts
    print(f"\nCHANGED RULE: allowed attempts = {allowed}")
    return verify_with_while(entries, allowed)


def verify_recursive(entries, index=0, attempts=0, max_attempts=3):
    """Recursive alternative; returns True if verified, otherwise False."""
    if attempts >= max_attempts:
        print("Recursive version: account locked for 30 minutes.")
        return False
    if index >= len(entries):
        print("Recursive version: no more entries supplied.")
        return False

    entry = entries[index]
    if entry.strip() == "":
        print("Recursive version: blank entry not counted.")
        return verify_recursive(entries, index + 1, attempts, max_attempts)

    print(f"Recursive attempt {attempts + 1}: {entry}")
    if entry == CORRECT_OTP:
        print("Recursive version: OTP verified.")
        return True
    return verify_recursive(entries, index + 1, attempts + 1, max_attempts)


def main():
    while_entries = ["", "111111", "222222", "333333"]
    for_entries = ["", "111111", "222222", "482913"]
    changed_entries = ["123123", "234234", "345345", "456456", "482913"]

    verify_with_while(while_entries)
    verify_with_for(for_entries)
    verify_with_security_question(
        changed_entries, security_answer="blue", correct_security_answer="blue"
    )
    print("\nRECURSIVE ALTERNATIVE")
    verify_recursive(["", "111111", "222222", "333333"])

    print("\nANALYSIS")
    print("while is natural when the number of input entries is not known in advance.")
    print("for range(max_attempts) is suitable when the number of counted attempts is fixed.")
    print("Incrementing the counter for blank input wrongly consumes an attempt.")
    print("Updating the counter after checking can allow too many attempts.")
    print("Loop time: O(a) for a counted attempts; loop extra space: O(1).")
    print("Recursive time: O(a); recursive call-stack space: O(a).")


if __name__ == "__main__":
    main()
