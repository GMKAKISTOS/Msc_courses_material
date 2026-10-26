#2:23:03 - https://www.youtube.com/watch?v=ix9cRaBkVe0

list1 = [1, 2, 3, 4, 5]

list1.append(6)

print()
print(list1)

list1.extend([7, 8, 9, 10])

print(list1)

list1.append([11, 12, 13, 14, 15])

print(list1)

print(list1[10])

print(list1[10][4])

list1.extend([16, [17, 18, 19, 20, [21, 22, 23, 24, 25, [26, 27, 28, 29, 30]]]])

print()
print(list1)
print(list1[12])
print(list1[12][4])
print(list1[12][4][5])
print(f"Sum: {sum(list1[12][4][5])}")
print(f"Count: {len(list1[12][4][5])}")
print(f"Average: {(sum(list1[12][4][5])) / len(list1[12][4][5])}")
print(f"Average with //: {(sum(list1[12][4][5])) // len(list1[12][4][5])}")

list1[12][4][5].pop()

list1[12][4][5].insert(len(list1[12][4][5]), 31)

print(list1)
print(f"Sum: {sum(list1[12][4][5])}")
print(f"Count: {len(list1[12][4][5])}")
print(f"Average: {(sum(list1[12][4][5])) / len(list1[12][4][5])}")
print(f"Average with //: {(sum(list1[12][4][5])) // len(list1[12][4][5])}")
print()

list2 = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10}
print(list2)
list2.add(11)
list2.add(11)
print(list2)
list2.pop()
print(list2)
list2.remove(10)
print(list2)
print()

list3 = (1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10)
print(list3)

print()
print(dir(list1))
print(dir(list2))
print(dir(list3))
#print(help(list1))
#print(help(list2))
#print(help(list3))
list4bool = 10 in list3 or 11 in list3
print()
print(list4bool)
list4bool = 9 in list3 and 10 in list3
print(list4bool)
list4bool = 10 in list3 and 11 in list3
print(list4bool)
list4bool = not(10 in list3 and 11 in list3)
print(list4bool)
list4bool = 11 in list3 or 12 in list3
print(list4bool)
list4bool = not(11 in list3 or 12 in list3)
print(list4bool)

print()
list5 = ["z", "b", "a", "g", "l"]
print(list5)
list5.sort()
print(list5)
list5.reverse()
print(list5)
pos = list5.index("g")
print(pos)
pos = list5.index("l")
print(pos)
countt = list5.count("z")
print(countt)
list5.clear()
print(list5)

#3:03:28 - https://www.youtube.com/watch?v=ix9cRaBkVe0

print()
dictionary = {"apple" : "food", "banana" : "food", "car" : "notfood"}

for key, value in dictionary.items():
    if(value == "food"):
        print(key, end = " ")
    else:
        print(-1, end = " ")
print()

for key in dictionary.keys():
    print(key, end = " ")
print()

for value in dictionary.values():
    print(value, end = " ")
print()

print(dictionary.get("apple"))

if dictionary.get("banana"):
    print("Exists!")
else:
    print("Not exists!")

if dictionary.get("onion"):
    print("Exists!")
else:
    print("Not exists!")

boolconverted = bool(dictionary.get("onion"))
if boolconverted:
    print("Exists!")
else:
    print("Not exists!")

boolconverted = bool(dictionary.get("banana"))
if boolconverted:
    print("Exists!")
else:
    print("Not exists!")

print(dictionary)

dictionary.update({"tost" : "food"})

print(dictionary)

dictionary.update({"car" : "notfoodupdated"})

print(dictionary)

dictionary.pop("banana")

print(dictionary)

dictionary.popitem()

print(dictionary)

dictionary.clear()

print(dictionary)

#3:19:42 - https://www.youtube.com/watch?v=ix9cRaBkVe0