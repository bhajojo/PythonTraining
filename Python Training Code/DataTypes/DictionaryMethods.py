ExampleDict = {"apple":"green","banana":"yellow","cherry":"red"}
ExampleDict2 = {"apple":"green","banana":"yellow","cherry":"red"}
print ExampleDict.__len__()
#print ExampleDict.fromkeys()
#ExampleDict.copy()
#ExampleDict.clear()

print ExampleDict
print ExampleDict.has_key("apple")
print ExampleDict.items()
print ExampleDict.values()

print cmp(ExampleDict,ExampleDict2)
