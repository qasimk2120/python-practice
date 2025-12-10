# def main():
#     x =  int(input("What's x? "))
#     print("x squared is ", square(x))
# def square(n):
#     # return n * n #here we also have pow function to calculate power of a number e.g.
#     return n * n
# if __name__ == "__main__":
#     main()

#assert in python allows us to sort of boldly claim that something is true
#Unit tests are typically tests for functins that you have written


def main():
    name = input("What's your name? ")
    print(hello(name))
def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()