def convert(time_str):
    """
    Convert a 24-hour time string (H:MM or HH:MM) to a float representing hours.
    Example: "7:30" -> 7.5
    """
    hours, minutes = map(int, time_str.split(":"))
    return hours + minutes / 60

def main():
    # Prompt the user for time
    time_input = input("Enter the time in 24-hour format (#:## or ##:##): ").strip()

    # Convert the input to hours as a float
    time_in_hours = convert(time_input)

    # Check which meal time it is
    if 7 <= time_in_hours <= 8:
        print("breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()
