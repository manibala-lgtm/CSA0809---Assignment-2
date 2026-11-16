"""
Q3 - Vehicle Registration Number Validator
Run: python q3_vehicle_validator.py
Only the permitted string operations are used for normalisation and validation.
"""

def normalise(text):
    """'tn 09 ab 1234' -> 'TN09AB1234'."""
    return text.strip().upper().replace(" ", "").replace("-", "")


def is_valid(reg):
    """Format: 2 letters + 2 digits + 1/2 letters + 4 digits."""
    if len(reg) not in (9, 10):
        return False

    state = reg[0:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    return (
        len(state) == 2
        and state.isalpha()
        and len(district) == 2
        and district.isdigit()
        and len(series) in (1, 2)
        and series.isalpha()
        and len(number) == 4
        and number.isdigit()
    )


def format_receipt(reg):
    if not is_valid(reg):
        raise ValueError("Cannot format an invalid registration number.")
    return reg[0:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


def main():
    test_inputs = [
        "tn 09 ab 1234",
        "KA-01-M-0007",
        "Tn09Ab1234",
        "TN9AB1234",
        "TN 22 1234 AB",
        "MH 12 XYZ 4567",
    ]

    print("INPUT PREDICTIONS / OBSERVED RESULTS")
    for raw in test_inputs:
        reg = normalise(raw)
        status = "valid" if is_valid(reg) else "INVALID"
        print(f"{raw:18} -> {reg:11} {status}")

    print("\nRECEIPT FORMAT")
    for raw in test_inputs:
        reg = normalise(raw)
        if is_valid(reg):
            print(format_receipt(reg))

    print("\nSTRING INQUIRY")
    sample9 = "TN09A1234"       # 9 characters
    sample10 = "TN09AB1234"     # 10 characters
    print("9-char s[-4:]:", sample9[-4:])
    print("9-char s[4:-4]:", sample9[4:-4])
    print("10-char s[-4:]:", sample10[-4:])
    print("10-char s[4:-4]:", sample10[4:-4])
    print("Strings are immutable: operations create a new string rather than changing the original.")
    original = "tn09ab1234"
    changed = original.upper()
    print("original:", original, "| upper result:", changed)

    print("\nALTERNATIVE REGEX CONCEPT")
    print(r're.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}", reg)')
    print("Slicing validation: O(L) time and O(1) auxiliary space.")
    print("Regex fullmatch: O(L) time for this fixed pattern; concise but pattern syntax may be less familiar.")


if __name__ == "__main__":
    main()
