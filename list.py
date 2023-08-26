# List is mutable

list1 = [3, 5, 32, 100, 6]
print(type(list1))
print(list1)

list1.sort()
print(list1)

list1.pop()
print(list1)

list1.append(90)
print(list1)

list1.extend([8, 65, 31])
print(list1)

list1[0] = 1000
print(list1)