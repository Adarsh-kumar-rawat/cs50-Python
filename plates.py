def is_valid(s: str) -> bool:
    # Rule 1: Length between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 3: Numbers can only be at the end, first number cannot be 0
    first_digit_index = None
    for i, char in enumerate(s):
        if char.isdigit():
            first_digit_index = i
            if char == '0':  # first number cannot be 0
                return False
            break

    if first_digit_index is not None:
        # Ensure all remaining characters are digits
        if not all(c.isdigit() for c in s[first_digit_index:]):
            return False

    # Rule 4: No punctuation, periods, or spaces (only letters and numbers)
    if not all(c.isalnum() for c in s):
        return False

    return True


plate = input("Plate: ")
if is_valid(plate):
    print("Valid")
else:
    print("Invalid")
