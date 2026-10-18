import math as m

print()

friends = 0
print(friends)
friends += 10
print("+ ->", friends)
friends = friends + 10
print("+ ->", friends)
friends -= 10
print("- ->", friends)
friends = friends - 10
print("- ->", friends)
friends = 10
friends *= 10
print("* ->", friends)
friends = 25
friends /= 10
print("/ ->", friends)
friends %= 10
print("% ->", friends)
friends = 25
friends //= 10
print("// ->", friends)
friends = friends ** 2
print("** ->", friends)
friends **= 2
print("** ->", friends)

print()
x = 3.14
y = -4
z = 5

result = round(x)
print(result)
result = abs(y)
print(result)
result = 5
result = pow(result, 2)
print(result)
result = 24
result = divmod(result, 7)
print(result)
result = max(x, y, z)
print(result)
result = min(x, y, z)
print(result)
result = m.pi
print(result)
result = m.e
print(result)
result = 49
result = m.sqrt(result)
print(result)
result = 7.6
result = m.ceil(result)
print(result)
result = 7.6
result = m.floor(result)
print(result)

while True:
    try:
        radius = float(input("\nEnter radius: "))
        if radius >= 0.0:
            circumference = 2 * m.pi * radius
            print(f"\nThe circumference is {circumference}cm!")
            print(f"The circumference is {round(circumference, 2)}cm! - (rounded)")
            break
    except ValueError:
        print("Invalid value!")

while True:
    try:
        radius = float(input("\nEnter the radius of a circle: "))
        if radius >= 0.0:
            area = m.pi * pow(radius, 2)
            print(f"\nThe area of the circle is {area}cm^2!")
            print(f"The area of the circle is {round(area, 2)}cm^2! - (rounded)")
            break
    except ValueError:
        print("Invalid value!")

while True:
    try:
        a = float(input("\nEnter side A: "))
        b = float(input("Enter side B: "))
        if a >= 0.0 and b >= 0.0:
            c = m.sqrt(pow(a, 2) + pow(b, 2))
            print(f"\nThe side C is {c}cm!")
            print(f"The side C is {round(c)}cm! - (rounded)")
            break
    except ValueError:
        print("Invalid value!")

#51:46 - https://www.youtube.com/watch?v=ix9cRaBkVe0