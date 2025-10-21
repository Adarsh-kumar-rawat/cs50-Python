import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y

        for attempt in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(correct)

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3.")
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:  # level == 3
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
