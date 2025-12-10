from assignments import convert,guage  # Make sure this imports the correct module
import pytest
def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("99/100") == 99

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("abc/3")
    with pytest.raises(ValueError):
        convert("3/abc")
    with pytest.raises(ValueError):
        convert("3")
def test_gauge():
    assert guage(100) == "F"
    assert guage(99) == "F"
    assert guage(1) == "E"
    assert guage(0) == "E"
    assert guage(50) == "50%"
    assert guage(25) == "25%"
    assert guage(75) == "75%"