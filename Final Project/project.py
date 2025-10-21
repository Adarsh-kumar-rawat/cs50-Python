import random

def main():
    """Main chatbot loop."""
    greet_user()
    name = ask_name()

    print(f"Nice to meet you, {name}! You can ask me things like:")
    print("- How are you?")
    print("- Tell me a joke")
    print("- What’s my name?")
    print("- Or type 'exit' to quit.")

    while True:
        user_input = get_user_input()
        if user_input.lower() in ["quit", "exit"]:
            say_goodbye(name)
            break
        response = generate_response(user_input, name)
        print(f"ChatMini: {response}")


def greet_user():
    """Greets the user at the start of the chat."""
    print("Hello! I'm ChatMini — your friendly mini chatbot!")


def ask_name():
    """Asks for the user's name."""
    name = input("What's your name? ").strip()
    if not name:
        name = "Friend"
    return name.capitalize()


def get_user_input():
    """Gets input from the user."""
    return input("You: ").strip()


def generate_response(user_input, name):
    """Generates a response based on the user input."""
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return f"Hello {name}!"
    elif "how are you" in user_input:
        return random.choice(["I'm doing great!", "Feeling chatty today!", "All systems operational!"])
    elif "your name" in user_input:
        return "I'm ChatMini — your mini chatbot!"
    elif "my name" in user_input:
        return f"Your name is {name}, of course!"
    elif "joke" in user_input:
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I told my computer I needed a break... and it froze.",
            "Why did the developer go broke? Because he used up all his cache!"
        ])
    else:
        return random.choice([
            "Hmm, I'm not sure I understand that.",
            "Can you rephrase that?",
            "Interesting! Tell me more."
        ])


def say_goodbye(name):
    """Ends the chat politely."""
    print(f"Goodbye, {name}! It was great chatting with you.")


if __name__ == "__main__":
    main()
