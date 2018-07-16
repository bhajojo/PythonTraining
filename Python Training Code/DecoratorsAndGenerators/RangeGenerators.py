def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

y= yrange(10)
for value in yrange(10):
     print(y.next())
