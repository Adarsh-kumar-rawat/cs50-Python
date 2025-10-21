from um import count

def test_single_um():
    assert count("hello, um, world") == 1

def test_multiple_ums():
    assert count("Um, I think, um, this is fine. UM!") == 3

def test_no_um():
    assert count("yummy, umbrella, hum") == 0

def test_um_with_punctuation():
    assert count("Well... um! Are you ready? Um.") == 2

def test_um_case_insensitive():
    assert count("uM um UM") == 3
