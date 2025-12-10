import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"(\d{1,3})\.\d({1,3})\.\d({1,3})$)"
    match = re.search(pattern, ip)
    if not match:
        return False
    else:
        parts=  match.groups()
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
    return True

def  test_valid_address():
    assert validate("192.168.9.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
def test_invalid_address():
    assert validate("192.168.9.256") == False
    assert validate("192.168.9") == False


if __name__ == "__main__":
    main()