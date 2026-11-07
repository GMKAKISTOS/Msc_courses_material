import numpy as np

print()
list1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(np.sum(list1))
print(np.mean(list1))
print(np.std(list1))
print(np.var(list1))
print(np.min(list1))
print(np.max(list1))
print(np.argmin(list1))
print(np.argmax(list1))
list2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np.sum(list2, axis = 0))
print(np.sum(list2, axis = 1))

#43:53 - https://www.youtube.com/watch?v=VXU4LSAQDSc

