from data_structures.linear_data_structures import UnorderedList


mylist = UnorderedList()

mylist.add(10)
mylist.add(20)
mylist.add(30)
mylist.add(40)
mylist.add(50)
mylist.add(60)

print(mylist.index(40))
print(mylist.index(50))
print(mylist.index(60))

mylist.insert(2, 45)

print(mylist.index(40))
print(mylist.index(45))
print(mylist.index(50))
print(mylist.index(60))

print(mylist.pop(0))
