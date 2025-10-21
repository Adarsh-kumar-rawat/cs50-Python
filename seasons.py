from datetime import date, datetime
import sys
import inflect  # pip install inflect

def main():
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ").strip()
    birth_date = parse_date(dob_str)
    if not birth_date:
        sys.exit("Invalid date format. Use YYYY-MM-DD.")

    minutes = age_in_minutes(birth_date)

    # Convert number to words, preserving hyphens and commas
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")  # no "and"

    # Capitalize first letter and append 'minutes'
    output = words.capitalize() + " minutes"
    print(output)

def parse_date(dob_str):
    """Parse a date string in YYYY-MM-DD format and return a date object, or None if invalid."""
    try:
        return datetime.strptime(dob_str, "%Y-%m-%d").date()
    except ValueError:
        return None

def age_in_minutes(birth_date):
    """Calculate the total number of minutes lived from birth_date to today."""
    today = date.today()
    delta_days = (today - birth_date).days
    minutes = delta_days * 24 * 60
    return minutes

if __name__ == "__main__":
    main()
