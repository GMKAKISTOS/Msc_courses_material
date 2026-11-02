import numpy as np

print()
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list1)

list2 = np.array(list1) * 2

list3 = []
for i in range(0, len(list2)):
    list3.append(int(list2[i]))
    #list3.append(list2[i])

#list3 = list2.tolist()
print(list3)

if len(list2) == len(list3):
    print("Same length!")
else:
    print("Different length!")

list4 = []
list5 = []
for i in range(0, len(list3)):
    if np.array(list3[i] <= 10):
        list4.append(list3[i])
    else:
        list5.append(list3[i])

print(list4)
print(list5)
sumnumbers1 = np.array(sum(list4))
print(sumnumbers1)
sumnumbers2 = np.array(sum(list5))
print(sumnumbers2)

print()
list6 = [1, 2, 3, 4, 5]
list7 = list6 * 2
print(list6)
print(list7)

list8 = []
for i in range(0, len(list6)):
    list6[i] = list6[i] * 2
    list8.append(list6[i])

print(list8)

print()

list9 = np.array([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]])

print(list9)
print(list9[1][1])
print(list9.ndim)
print(list9.shape)

print()
list10 = np.array([[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
                   [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
                   [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]]])

print(list10)
print(list10.ndim)
print(list10.shape)
print()
print(list10[1])
print(list10[1][1])
print(list10[1][1][1])

#10:00 - https://www.youtube.com/watch?v=VXU4LSAQDSc