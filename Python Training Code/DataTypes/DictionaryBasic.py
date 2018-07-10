ExampleDict = {"apple":"green","banana":"yellow","cherry":"red" ,"apple1":"red"}

print(ExampleDict)
print(ExampleDict["apple"])
#print(ExampleDict["bharat"])
print(ExampleDict.pop('apple'))
print(ExampleDict)

print(ExampleDict.keys())
print(ExampleDict.get('cherry'))
#print(ExampleDict.get['bharat'])

ExampleDict["mango"]="yellow"
print(ExampleDict)

del(ExampleDict["mango"])

print(ExampleDict)
