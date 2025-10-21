def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            # Case 1: Numeric format (MM/DD/YYYY)
            if "/" in date:
                month, day, year = date.split("/")
            # Case 2: Text format (Month Day, Year)
            elif "," in date:
                month_name, day_year = date.split(" ", 1)
                day, year = day_year.replace(",", "").split(" ")
                month = months.index(month_name) + 1
            else:
                raise ValueError

            month = int(month)
            day = int(day)
            year = int(year)

            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError

            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except (ValueError, IndexError):
            continue


if __name__ == "__main__":
    main()
