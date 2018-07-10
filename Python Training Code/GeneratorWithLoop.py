def rev_str(my_str):
    length = len(my_str)
    print length-1

    for i in range(27,-1,-1):


        yield my_str[i]

for char in rev_str("Any other characters to test"):
     print(char)
