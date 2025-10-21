def main():
    names = []

    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        print()  # clean newline, not an error
        pass  # ensure exit code 0

    print(f"Adieu, adieu, to {format_names(names)}")


def format_names(names):
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}"
    else:
        return f"{', '.join(names[:-1])}, and {names[-1]}"


if __name__ == "__main__":
    main()
