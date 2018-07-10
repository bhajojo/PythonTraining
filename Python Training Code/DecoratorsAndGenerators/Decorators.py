def my_decorator(functionname): #decorator function
    def wrapper(): #inner function
        print("Something is happening before some_function() is called.")
        functionname()
        print("Something is happening after some_function() is called.")
    return wrapper

def anyfunctionname():
    print("inside decorator function!")

def functionName1():
    print("inside decorator function1!")

def functionname2():
    print("inside decorator function2!")


retunparameter = my_decorator(anyfunctionname) #call to function
retunparameter()

retunparameter1 = my_decorator(functionName1) #call to function
retunparameter1()

retunparameter2 = my_decorator(functionname2) #call to function
retunparameter2()


def funcExample(num):
    print num
funcExample(5) #call to function