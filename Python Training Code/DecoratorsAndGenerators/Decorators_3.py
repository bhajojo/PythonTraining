def decorator_func(some_func):
    # define another wrapper function which modifies some_func
    def wrapper_func():
        print("Wrapper function started")

        some_func()

        print("Wrapper function ended")

    return wrapper_func  # Wrapper function add something to the passed function and decorator returns the wrapper function


def say_hello():
    print ("Hello")


say_hello = decorator_func(say_hello)

say_hello()

# Output:
#  Wrapper function started
#  Hello
#  Wrapper function started