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

print()
list2 = np.array([[30, 45, 18, 50, 13, 20, 25, 17, 35, 60],
         [31, 46, 16, 54, 22, 27, 36, 43, 47, 63]])

print(f"{list2[0]} - {list2[1]}")
teenagers = list2[list2 < 18]
print(teenagers)
adults = list2[list2 >= 18]
print(adults)
adults = list2[(list2 >= 18) & (list2 <= 60)]
print(adults)
adults = list2[(list2 >= 18) | (list2 <= 60)]
print(adults)
olders = list2[list2 > 60]
print(olders)
numberseven = list2[list2 % 2 == 0]
print(numberseven)
numbersodd = list2[list2 % 2 != 0]
print(numbersodd)
adults1 = np.where(list2 <= 30, list2, 0)
print(adults1)

print()

rn = np.random.default_rng()

print(rn.integers(1, 10))
print(rn.integers(low = 1, high = 100))
print(rn.integers(low = 1, high = 100, size = 20))
print(rn.integers(low = 1, high = 100, size = (4, 4)))

rn = np.random.default_rng(seed = 1)# same results
print(rn.integers(1, 10))
print()
print(np.random.uniform())
print(np.random.uniform(low = -1 , high = 1, size = 3))
print(np.random.uniform(low = -1 , high = 1, size = (3, 2)))
np.random.seed(seed = 1)
print(np.random.uniform(low = -1 , high = 1, size = (3, 2)))

print()
rng = np.random.default_rng()
list3 = [1, 2, 3, 4, 5]
print(list3)
rng.shuffle(list3)
print(list3)

print()
list4 = np.array(["apple", "banana", "orange", "pineapple", "coconut"])
rng = np.random.default_rng()
fruits = rng.choice(list4)
print(fruits)
fruits = rng.choice(list4, size = 3)
print(fruits)
fruits = rng.choice(list4, size = (3, 2))
print(fruits)

#0:00 - https://www.youtube.com/watch?v=VXtjG_GzO7Q - pandas