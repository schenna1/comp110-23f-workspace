#initializing a list
# name: list[type] = [objects]
list1: list[int] = [1, 2, 3, 5]

#update value at index
# name[index] = value
list1[3] = 4

#print lenght
print(len(list1))

#add and remove
# name.append(value), name.pop(index)
list1.append(5)
list1.pop(4)

print(list1)