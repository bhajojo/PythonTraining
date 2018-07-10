fruits=["apple","Mango","Strarawberry","Tomato","Banana","Cherry"]
for x in fruits:
    print "inside For Loop"
    if x== "Banana":
        print "I will not print banana value"
        continue
    print x
print "Out of For Loop"