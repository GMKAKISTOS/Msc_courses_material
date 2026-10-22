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

print()
weather = "cold" or "medium" or "hot"

if weather == "cold":
    print("Cold weather!")
elif weather == "medium":
    print("Medium weather!")
elif weather == "hot":
    print("Hot weather!")
elif weather not in ("cold", "medium", "hot"):
    print("Something else!")

print(f"Weather is {weather}!")

weather = "medium" or "cold" or "hot"

if weather == "cold":
    print("Cold weather!")
elif weather == "medium":
    print("Medium weather!")
elif weather == "hot":
    print("Hot weather!")
elif weather not in ("cold", "medium", "hot"):
    print("Something else!")

print(f"Weather is {weather}!")

weather = "hot" or "cold" or "medium"

if weather == "cold":
    print("Cold weather!")
elif weather == "medium":
    print("Medium weather!")
elif weather == "hot":
    print("Hot weather!")
elif weather not in ("cold", "medium", "hot"):
    print("Something else!")

print(f"Weather is {weather}!")

weather = not "hot" or not "cold" or not "medium"

if weather == "cold":
    print("Cold weather!")
elif weather == "medium":
    print("Medium weather!")
elif weather == "hot":
    print("Hot weather!")
elif weather not in ("cold", "medium", "hot"):
    print("Something else!")

print(f"Weather is {weather}!")

print()
age = 29
isStudent = True
statusOfJob = "Unemployed"

if age >= 29 and isStudent is True and statusOfJob == "Employed":
    print("This guy makes money!")
elif age < 29 and isStudent is True and not statusOfJob == 'Employed':
    print("This guy doesn't makes money!")
else:
    print("Unknown situation of this guy!")

age = 28
isStudent = not(isStudent)
statusOfJob = "Unemployed"

if age >= 29 and isStudent is True and statusOfJob == "Employed":
    print("This guy makes money!")
elif age < 29 and isStudent is False and not statusOfJob == 'Employed':
    print("This guy doesn't makes money!")
else:
    print("Unknown situation of this guy!")

age = 29
isStudent = True
statusOfJob = "Unemployed"

if age >= 29 or isStudent is False or statusOfJob == "Employed":
    print("This guy makes money!")
elif age < 29 or isStudent is True or not statusOfJob == 'Employed':
    print("This guy doesn't makes money!")
else:
    print("Unknown situation of this guy!")

age = 28
isStudent = not(isStudent)
statusOfJob = "Unemployed"

if age >= 29 or isStudent is True or statusOfJob == "Employed":
    print("This guy makes money!")
elif (age < 29 or isStudent is True) and (not (not statusOfJob == 'Employed')):
    print("This guy doesn't makes money!")
else:
    print("Unknown situation of this guy!")

if age >= 29 or isStudent is True or statusOfJob == "Employed":
    print("This guy makes money!")
elif (age < 29 or isStudent is True) and (not statusOfJob == 'Employed'):
    print("This guy doesn't makes money!")
else:
    print("Unknown situation of this guy!")

print()
t = 0 < 20 > 10
print(f"1: {t}")
t = 0 < 20 < 10
print(f"2: {t}")
print(f"3: {not t}")
print(f"4: {not (not t)}")
print(f"5: {not (not (not t))}")
print(f"6: {t is True}")
print(f"7: {t is not True}")
print(f"8: {t is False}")
print(f"9: {t is not False}")

#1:21:29 - https://www.youtube.com/watch?v=ix9cRaBkVe0

print()
f = 20
print("Positive!" if f > 0 else "Negative!" if f < 0 else "Zero!")
f = -20
print("Positive!" if f > 0 else "Negative!" if f < 0 else "Zero!")
f = 0
print("Positive!" if f > 0 else "Negative!" if f < 0 else "Zero!")
f = 10
result = "Even!" if f % 2 == 0 else "Odd!"
print(result)
f = 11
result = "Even!" if f % 2 == 0 else "Odd!"
print(result)

#1:27:03 - https://www.youtube.com/watch?v=ix9cRaBkVe0