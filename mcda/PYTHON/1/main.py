#def print_name(name):
#    print("Hi, my name is " + name + "!")
from math import ceil, floor
from collections import namedtuple
from selectors import SelectSelector

#def print_age(age):
#    print(f"I am " + str(age) + " years old!")

#def print_status_age(age):
#    status = "He/she is young!" if age < 18 else "He/she is big!" if age >= 18 and age < 50 else "he/she is old!"
#    return status

#if __name__ == "__main__":
#def main():
#    print()
#    print_name("panos")
#    print_age(29)
#    print(print_status_age(29))
#    print()
#    print_name("nikos")
#    print_age(50)
#    print(print_status_age(50))
#    print()
#    print_name("eleni")
#    print_age(17)
#    print(print_status_age(17))

#main()

firstName = "panos"
food = "pizza"
email = "panos_chron@hotmail.com"
age = 29
quantity = 3
#print("\nHello " + firstName + "!")
#print("Hello", firstName, "!")
print(f"\nHello {firstName}!")
print(f"You like {food}!")
print(f"Your email is {email}")
print(f"You are {age} years old!")
print(f"You are buying {quantity} items!")

firstName, food, email, age, quantity  = "nikos", "ice cream", "nick_chron@hotmail.com", 30, 4
print(f"\nHello {firstName}!")
print(f"You like {food}!")
print(f"Your email is {email}")
print(f"You are {age} years old!")
print(f"You are buying {quantity} items!")

numberOfStudents = 30
print(f"\nThere are {numberOfStudents} students in the class!")
print(f"There are {(numberOfStudents * "2")} students in the class!")
print(f"There are {numberOfStudents * int("2")} students in the class!")

price = 10.99
gpa = 3.2
distance = 5.5
print(f"\nPrice is ${price}!")
print(f"GPA is: {gpa}!")
print(f"Distance is {distance}!")
print(f"Distance is {round(distance, 0)}!")
print(f"Distance is {round(distance, 1)}!")
print(f"Distance is {ceil(distance)}!")
print(f"Distance is {floor(distance)}!")
print(f"Distance is {abs(distance)}!")

isStudent = True
age = 50
print(f"Are you a student? -> {isStudent}!")
print(f"Are you a student? -> {isStudent if age == 50 else not isStudent}!")
print(f"Are you a student? -> {isStudent if age == 30 else not isStudent}!")
print(f"Are you a student? -> {isStudent if age == 30 else False}!")
print(f"Are you a student? -> {not isStudent if age == 30 else not False}!")
print(f"Status: {0 >= age >= -100}!")
print(f"Status: {0 >= -age >= -100}!")

forSale = True
status = "This item is for sale!" if forSale else "This item is not for sale!"
print(status)
forSale = False
status = "This item is for sale!" if forSale else "This item is not for sale!"
print(status)

Constants = namedtuple("Constants", ["pi"])
constants = Constants(pi = 3.14159)
print(f"pi: {constants.pi}!")

#16:10 video time

stringWithNumbers = "abc123"
withNumbers = int(stringWithNumbers[3:])
print(f"\nString: {stringWithNumbers} - Number: {withNumbers}")
print(f"{type(stringWithNumbers)} - {type(withNumbers)}")
stringWithNumbers = "abc123!"
withNumbers = int(stringWithNumbers[3:6])
print(f"String: {stringWithNumbers} - Number: {withNumbers}")
print(f"{type(stringWithNumbers)} - {type(withNumbers)}")
stringWithNumbers = "123!abc"
withNumbers = int(stringWithNumbers[:3])
print(f"String: {stringWithNumbers} - Number: {withNumbers}")
print(f"{type(stringWithNumbers)} - {type(withNumbers)}")
withNumbers = int(stringWithNumbers[:-4])
print(f"String: {stringWithNumbers} - Number: {withNumbers}")
print(f"{type(stringWithNumbers)} - {type(withNumbers)}")
stringWithNumbers = "1a2b3c!"
withNumbers = int(stringWithNumbers[0:6:2])
print(f"String: {stringWithNumbers} - Number: {withNumbers}")
print(f"{type(stringWithNumbers)} - {type(withNumbers)}")

name = "panos chron"
age = 29
gpa = 3.2
isMscStudent = True
print(f"\n{type(name)} - {type(age)} - {type(gpa)} - {type(isMscStudent)}")
print(f"{name} - {age} - {gpa} - {isMscStudent}")
age = float(age)
gpa = int(gpa)
print(f"{type(name)} - {type(age)} - {type(gpa)} - {type(isMscStudent)}")
print(f"{name} - {age} - {gpa} - {not isMscStudent}")
age = str(age)
gpa = str(gpa)
print(f"{type(name)} - {type(age)} - {type(gpa)} - {type(isMscStudent)}")
print(f"{name} - {age} - {gpa} - {not isMscStudent}")
name2 = name[0:5]
name3 = name[5:6]
name4 = name[6:11]
print(f"{name2}{name3}{name4}")
age1 = 29
age2 = str(age1) + "1"
print(f"age2: {age2}")
age3 = int(age2) - 262
print(f"age3: {age3}")

print()
giveFirstName = str(input("Give firstname: "))
while not giveFirstName.isalpha():
    giveFirstName = str(input("Give firstname: "))
giveSecondName = str(input("Give lastname: "))
while not giveSecondName.isalpha():
    giveSecondName = str(input("Give lastname: "))
while True:
    try:
        giveAge = float(input("Give age: "))
        #if giveAge.__float__():
        if giveAge >= 0.0 and giveAge <= 95:
            giveFirstName = giveFirstName.capitalize()
            giveSecondName = giveSecondName.capitalize()
            break
    except ValueError:
        print("Invalid value!")
while True:
    try:
        giveGrossSalary = float(input("Give salary: "))
        #if giveGrossSalary.__float__():
        if giveGrossSalary >= 0.0:
            giveNetSalary = giveGrossSalary - ( giveGrossSalary * 0.20)
            break
    except ValueError:
        print("Invalid value!")
print(f"{giveFirstName} - {giveSecondName} - {giveAge} years old - ${giveNetSalary}")

#32:42 - https://www.youtube.com/watch?v=ix9cRaBkVe0



