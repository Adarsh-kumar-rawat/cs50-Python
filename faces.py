def convert(text: str) -> str:
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input("Enter a message: ")
    converted = convert(user_input)
    print(converted)

if __name__ == "__main__":
    main()
