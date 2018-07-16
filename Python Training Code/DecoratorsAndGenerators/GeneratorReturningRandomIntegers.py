import random


def lottery():
    # returns 6 numbers between 1 and 40
    print ("for Loop")
    for i in range(6):
        yield random.randint(1, 100)

    print ("7th value")
    # returns a 7th number between 1 and 15
    return

    print ("8th value")
    yield random.randint(100, 150)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))