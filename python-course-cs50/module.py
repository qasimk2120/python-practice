##example module##
def main():
    hello("World!")
    goodbye("World!")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

 ##This is a special variable whose value is automatically set by Python to be,quote, unquote, "main" when you run a file from the command line
if __name__ == "__main__": 
    main()