import numpy as np

print()
list1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8],
                  [9, 10, 11, 12], [13, 14, 15, 16]])

print(list1)
print()
print(list1[:, :: 2])
print()
print(list1[:, :: -1])

print()
list2 = np.array([1, 2, 3, 4])

print(list2 + 1)
print(list2 - 2)
print(list2 * 2)
print(list2 / 2)
print(list2 ** 2)

print()
list3 = np.array([5.754, 6.412, 9, 25])
print(np.sqrt(list3))
print(np.round(list3))
print(np.round(list3, 2))
print(np.floor(list3))
print(np.ceil(list3))
print(np.pi)
print()

list4 = np.array([1, 2, 3, 4])
print(np.pi * list4 ** 2)

print()
list5 = np.array([1, 2, 3, 4])
list6 = np.array([5, 6, 7, 8])
print(list5 + list6)
print(list5 - list6)
print(list5 * list6)
print(list5 / list6)
print(list5 ** list6)

print()

scores = np.array([20, 15, 30, 100, 150, 5])
print(scores == 100)
print(scores[scores < 40])
print(np.sort(scores[scores < 40]))

#33:25 - https://www.youtube.com/watch?v=VXU4LSAQDSc

