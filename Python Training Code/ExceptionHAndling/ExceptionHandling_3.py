import NegativeAgeException
def enterage(age):
    if age < 0:
        raise NegativeAgeException("Only positive integers are allowed")
    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")
try:
    num = int(input("Enter your age: "))
    enterage(num)
except NegativeAgeException:
    print("Only positive integers are allowed")

