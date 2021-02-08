from data_structures.linear_data_structures import OrderedList


mylist = OrderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.remove(17)

print(mylist.size())
print(mylist.index(26))