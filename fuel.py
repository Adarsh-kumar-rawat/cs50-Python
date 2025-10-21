def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            # Reject invalid cases
            if y == 0 or x > y or x < 0 or y < 0:
                raise ValueError
            percentage = round((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

if __name__ == "__main__":
    main()
