try:
    n = raw_input("Please enter an integer: ")
    n = int(n)
    print n
    dividebyZero = n/0
except ValueError:
    print("No valid integer! Please try again ...")

except ZeroDivisionError:
    print("Division by zero is error !!")
finally:
    print("This will execute no matter what")
