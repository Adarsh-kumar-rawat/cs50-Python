from numb3rs import validate

def test_valid_ips():
    # Common valid addresses
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("140.247.235.144") == True
    assert validate("1.2.3.4") == True

def test_invalid_ips():
    # Out-of-range numbers
    assert validate("256.255.255.255") == False
    assert validate("64.128.256.512") == False
    assert validate("1.1.1.11111") == False
    # Wrong number of parts
    assert validate("8.8.8") == False
    assert validate("10.10.10.10.10") == False
    # Non-numeric or garbage
    assert validate("cat") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    # Leading zeros
    assert validate("000.001.010.100") == False
    assert validate("01.2.3.4") == False
