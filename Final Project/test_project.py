# test_project.py

from project import generate_response

def test_generate_response_basic():
    assert "Hello" in generate_response("hello", "Alice")
    assert "ChatMini" in generate_response("your name", "Bob")
    assert "Bob" in generate_response("my name", "Bob")

def test_generate_response_joke():
    response = generate_response("tell me a joke", "Sam")
    assert isinstance(response, str)
    assert len(response) > 0

def test_generate_response_unknown():
    response = generate_response("blah blah", "Eve")
    assert response in [
        "Hmm, I'm not sure I understand that.",
        "Can you rephrase that?",
        "Interesting! Tell me more."
    ]
