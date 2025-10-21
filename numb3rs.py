import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Split by dots
    parts = ip.split(".")

    # Must have exactly four parts
    if len(parts) != 4:
        return False

    for part in parts:
        # Each part must be numeric
        if not part.isdigit():
            return False

        num = int(part)

        # Each number must be 0-255
        if num < 0 or num > 255:
            return False

        # Leading zeros are invalid (except "0")
        if len(part) > 1 and part[0] == "0":
            return False

    return True

if __name__ == "__main__":
    main()
