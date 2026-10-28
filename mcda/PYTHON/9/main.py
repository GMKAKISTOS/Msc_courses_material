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