#number.py
# try, except, else , pass, raise keyword, still to be done
#exceptions

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()

