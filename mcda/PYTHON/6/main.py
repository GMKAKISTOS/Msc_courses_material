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