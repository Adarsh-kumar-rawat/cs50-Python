from bank import value

def test_hello_lowercase():
    assert value("hello") == 0
    assert value("hello there") == 0

def test_hello_uppercase():
    assert value("HELLO") == 0
    assert value("Hello World") == 0

def test_h_not_hello():
    assert value("hi") == 20
    assert value("Howdy") == 20
    assert value("hmm") == 20

def test_other_starting_letters():
    assert value("good morning") == 100
    assert value("apple") == 100
    assert value("zebra") == 100

def test_mixed_cases():
    assert value("hElLo everyone") == 0
    assert value("HoW are you") == 20
    assert value("Greetings") == 100
