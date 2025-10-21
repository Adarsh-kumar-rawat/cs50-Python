import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    """
    Count occurrences of 'um' as a whole word, case-insensitively.
    """
    # \b ensures word boundaries, re.I for case-insensitive
    return len(re.findall(r'\bum\b', s, re.IGNORECASE))

if __name__ == "__main__":
    main()
