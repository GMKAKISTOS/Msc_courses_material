#4:56:17 - https://www.youtube.com/watch?v=ix9cRaBkVe0

print()
def weekend(day):
    if day == 1:
        print("It's Sunday!")
    elif day == 2:
        print("It's Monday!")
    elif day == 3:
        print("It's Tuesday!")
    elif day == 4:
        print("It's Wednesday!")
    elif day == 5:
        print("It's Thursday!")
    elif day == 6:
        print("It's Friday!")
    elif day == 7:
        print("It's Saturday!")
    else:
        print("It's not a day!")

weekend(5)

def weekday(day):
    match (day):
        case 1:
            print("It's Saturday!")
        case 2:
            print("It's Monday!")
        case 3:
            print("It's Tuesday!")
        case 4:
            print("It's Wednesday!")
        case 5:
            print("It's Thursday!")
        case 6:
            print("It's Friday!")
        case 7:
            print("It's Saturday!")
        case _:
            print("It's not a day!")

weekday(6)
weekday(8)

def weekday2(day):
    match (day):
        case 1 | 2:
            print("It's Saturday or Monday!")
        case 3 | 4:
            print("It's Tuesday or Wednesday!")
        case 5 | 6 | 7:
            print("It's Thursday or Friday or Saturday!")
        case _:
            print("It's not a day!")

print()
weekday2(2)
weekday2(3)
weekday2(6)
weekday2(10)

print()
a, b, c, d, e = 0, 1, 2, 3, 4

print(a ** a)
print(b ** b)
print(c ** c)
print(d ** d)
print(e ** e)

print()
def function1():
    return 4
def function2():
    return 5
result = function1() * function2()
print(f"result: {result}!")




