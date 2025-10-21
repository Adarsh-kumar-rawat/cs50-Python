📝 README.md
# ChatMini – A Mini Chatbot
#### Video Demo: [https://youtu.be/MiUD5aibjIg](https://youtu.be/MiUD5aibjIg)
#### Author:
**Name:** Adarsh Kumar Rawat
**GitHub:** Adarsh-kumar-rawat
**edX:** darsh_7e
**City & Country:** Kanpur, India
**Date Recorded:** 21-10-2025

---

## 🧠 Description

**ChatMini** is a lightweight and interactive chatbot written in Python.
It can engage in small conversations, tell jokes, remember your name, and exit politely — all through simple text interaction.

This project demonstrates Python fundamentals such as:
- Conditional statements
- Loops
- String handling
- Randomized responses
- Function modularity
- Automated testing with `pytest`

---

## 🤖 Features

- **Personalized Greetings:** Learns and uses your name
- **Conversation:** Responds to greetings and questions
- **Jokes:** Tells random programming jokes
- **Exit Commands:** Type “exit” or “quit” to end the chat politely
- **Error Handling:** Manages unknown inputs with friendly replies

---

## 🧩 How It Works

`project.py` contains:
- `main()` — Runs the chatbot loop
- `greet_user()` — Greets the user
- `ask_name()` — Asks for and stores the user’s name
- `get_user_input()` — Takes continuous input from the user
- `generate_response()` — Determines the chatbot’s reply
- `say_goodbye()` — Ends the session gracefully

---

### 💬 Example Chat


Hello! I'm ChatMini — your friendly mini chatbot!
What's your name? Adarsh
Nice to meet you, Adarsh! You can ask me things like:

How are you?

Tell me a joke

What’s my name?

Or type 'exit' to quit.
You: hello
ChatMini: Hello Adarsh!
You: tell me a joke
ChatMini: Why do programmers prefer dark mode? Because light attracts bugs!
You: exit
Goodbye, Adarsh! It was great chatting with you.


---

## 🧪 Testing

To run tests:
```bash
pytest test_project.py


Covers:

Greeting and name recognition

Joke generation

Handling unknown inputs

📁 File Structure
project/
│
├── project.py          # Main chatbot code
├── test_project.py     # Automated tests
├── README.md           # Documentation
└── requirements.txt    # Dependencies

🏁 Conclusion

ChatMini is a fun, terminal-based chatbot showcasing core Python skills and clean design.
Built and demonstrated proudly from Kanpur, India 🇮🇳 as part of the CS50P final project.

🎬 Watch demo: https://youtu.be/MiUD5aibjIg
