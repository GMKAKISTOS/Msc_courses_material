#1:51:55 - https://www.youtube.com/watch?v=ix9cRaBkVe0

i = 1
while i <= 10:
    if(i != 10):
        if (i == 1):
            print()
            print(i, end = " ")
        else:
            print(i, end = " ")
    else:
        print(i, end = "")
        print()
    i = i + 1

i = 1
status = True
while status:
    if(i == 10):
        print(i, end = "")
    else:
        if(i == 1):
            print()
            print(i, end = " ")
        else:
            print(i, end = " ")
    i = i + 1
    if( i == 11):
        print()
        status = False

i = 1
while True:
    if(i == 10):
        print(i, end = "")
    else:
        if(i == 1):
            print()
            print(i, end = " ")
        else:
            print(i, end = " ")
    i = i + 1
    if( i == 11):
        print()
        break

z = 0
while True:
    if(z == 0):
        print()
        name = str(input("Give name: "))
        if(name not in ("panagiwths")):
            z += 1
            print(f"Name {z}: {name}")
        else:
            break
    else:
        name = str(input("Give name: "))
        if(name not in ("panagiwths")):
            z += 1
            print(f"Name {z}: {name}")
        else:
            z = 0
            break

for i in range(1, 11):
    if i == 1:
        print()
        print(i, end=" ")
    elif i == 10:
        print(i, end="")
        print()
    else:
        print(i, end = " ")

for i in reversed(range(1, 11)):
    if i == 1:
        print(i, end="")
        print()
    elif i == 10:
        print()
        print(i, end=" ")
    else:
        print(i, end = " ")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list1:
    if i == 1:
        #print(i, end="")
        #print()
        print()
        print(i, end=" ")
    elif i == 10:
        #print()
        #print(i, end=" ")
        print(i, end="")
        print()
    else:
        print(i, end = " ")

list1.reverse()

for i in list1:
    if i == 1:
        print(i, end="")
        print()
        #print()
        #print(i, end=" ")
    elif i == 10:
        print()
        print(i, end=" ")
        #print(i, end="")
        #print()
    else:
        print(i, end = " ")

for i in range(0, 11, 2):
    if i % 2 == 0 and i == 0:
        print()
        print(i, end = " ")
    elif i % 2 == 0 and i == 10:
        print(i, end = "")
        print()
    elif i % 2 == 0:
        print(i, end = " ")

for i in range(1, 12, 2):
    if i % 2 != 0 and i == 1:
        print()
        print(i, end = " ")
    elif i % 2 != 0 and i == 11:
        print(i, end = "")
        print()
    elif i % 2 != 0:
        print(i, end = " ")

for i in range(0, 22):
    if i % 2 != 0:
        continue
    else:
        if(i == 0):
            print()
            print(i, end = " ")
        elif(i == 20):
            print(i, end = "")
            print()
        else:
            print(i, end = " ")

for i in range(0, 22):
    if i % 2 == 0:
        continue
    else:
        if(i == 1):
            print()
            print(i, end = " ")
        elif(i == 21):
            print(i, end = "")
            print()
        else:
            print(i, end = " ")

for i in range(1, 11):
    print()
    for j in range (i, 11):
        print((i + j), end = " ")
print()

for i in range(4):
    print()
    for j in range(4):
        print("*", end = "")
print()

#2:23:03 - https://www.youtube.com/watch?v=ix9cRaBkVe0