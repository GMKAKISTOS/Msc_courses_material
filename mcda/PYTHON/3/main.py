x = 3 % 2 == 1
if x:
    print("\nTrue situation!")
else:
    print("\nFalse situation!")

x = 3 % 3 == 1
if x:
    print("True situation!")
else:
    print("False situation!")

x = 10 / 2 == 4 or 10 / 2 == 5
y = 10 % 6 == 4 and 10 % 3 == 1

if x:
    print("True situation! - 1")
    if y:
        print("True situation! - 2")
    else:
        print("False situation! - 2")
else:
    print("False situation! - 1")

x = int(input("\nEnter a number: "))

if 10 > x:
    print("ok! - 1")
elif 10 < x:
    print("ok! - 2")
else:
    print("not ok!")

stringx = "ok! - 1" if 10 < x  else "ok! - 2"  if 10 > x else "not ok!"
print(stringx)

print()
list1 = [1, 2, 3, 4, 5, 6]

#for i in range(1, len(list1)):
for i in list1:
    if(i % 2 == 0):
        print(i, end=" ")
    if(i == len(list1)):
        print()

#1:14:00 - https://www.youtube.com/watch?v=ix9cRaBkVe0

print()
x = not(not( 10 / 2 == 4 or 10 / 2 == 5))
y = not(10 % 6 == 4 and 10 % 3 == 1)

if x:
    print("True situation! - 1")
    if y:
        print("True situation! - 2")
    else:
        print("False situation! - 2")
else:
    print("False situation! - 1")