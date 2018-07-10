def my_gen():
    n=1

    print("this is printed first")
    yield n

    n= n+1
    print("this is printed second")
    yield n

    n = n + 1
    print("this is printed third")
    yield n

    n = n + 1
    print("this is printed fourth")
    yield n

a= my_gen()

print next(a)
print next(a)
print next(a)
print next(a)
