list = ['physics', 'chemistry', 1997, 2000,'python'];

#Check Append method
list.append("mathematics")
print(list[4])

#Remove the element from the list
list.remove('physics')
print (list)
print(list[0])

#Insert a value at index location 2
list.insert(2,'python')
print (list)

#Sort the items in the list
list.sort()
print (list)

#Pop will remove the element based on the index given
print(list.pop(3))
print (list)

## Returns the index of the element in the list
print(list.index('python'))
print(list.count("python"))

#Reverse the items in the List
list.reverse()
print list

