import numpy as np

print()
list1 = np.array([[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
         [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
         [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]]])

print(np.array(list1[2]))
print(np.array(list1[2][1]))
print(np.array(list1[2][1][2]))
print()
print(list1[2])
print(list1[2][1])
print(list1[2][1][0])

print()
word = list1[0, 0, 0]
print(word)

word = list1[1][2][0] + list1[0][0][0] + list1[1][1][1] + list1[1][1][2] + list1[2][0][0]
print(word)
print()

list2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8],
                 [9, 10, 11, 12], [13, 14, 15, 16]])

print(list2)
print()
print(list2[0])
print(list2[-1])
print()
print(list2[0:3])
print()
print(list2[0::2])
print()
print(list2[1::2])
print()
print(list2[::-2])
print()
print(list2[:, 0])
print(list2[:, 1])
print(list2[:, 2])
print(list2[:, 3])
print(list2[0, :])
print(list2[1, :])
print(list2[2, :])
print(list2[3, :])
print()
print(list2[:, 0:3])
print()
print(list2[0:3, :])

#20:00 - https://www.youtube.com/watch?v=VXU4LSAQDSc