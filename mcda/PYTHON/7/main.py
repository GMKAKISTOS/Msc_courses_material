import random as rand
import datetime as dt

#3:19:42 - https://www.youtube.com/watch?v=ix9cRaBkVe0

print()
randomnumber = rand.randint(0, 100)

print(f"random number: {randomnumber}!")

status = "third age!" if randomnumber >= 70 else "second age!" if randomnumber > 50 and randomnumber < 70 else "first age!"
print(f"status: {status}")

print()
low = int(input("Give low: "))
high = int(input("Give high: "))

randomnumber = rand.randint(low, high)

print(f"random number: {randomnumber}!")

status = "third age!" if randomnumber >= 70 else "second age!" if randomnumber > 50 and randomnumber < 70 else "first age!"
print(f"status: {status}")

print()
choices = ("bannana", "apple", "strawberry", "pineapple")

print(f"random choice: {rand.choice(choices)}!")

choices2 = ["Z", "W", "B", "A"]
rand.shuffle(choices2)
print(f"random choices: {choices2}!")

#3:52:12 - https://www.youtube.com/watch?v=ix9cRaBkVe0

print()
def function1():
    return "My name is"
print(f"{function1()} panos!")
choices3 = ("nikolaos", "panagiwths", "swthrhs", "alexandros", "ioannis")
name = rand.choice(choices3)
def function2(name):
    return f"My name is {name}!"
print(function2(name))
name = rand.choice(choices3)
print(function2(name))
name = rand.choice(choices3)
print(function2(name))

print()
choices4 = (True, False)
jobstatus = rand.choice(choices4)
def function3(myname, myage, myjobstatus):
    print(f"my name: {myname}!")
    print(f"my age: {myage}!")
    myagestatus = "third age!" if randomnumber >= 70 else "second age!" if randomnumber > 50 and randomnumber < 70 else "first age!"
    print(f"agestatus: {myagestatus}")
    if myage >= 18:
        if myjobstatus is False:
            myjobstatus = True
            print("Converted myjobstatus to True!")
            print(f"jobstatus: {myjobstatus}!")
        else:
            print(f"jobstatus: {myjobstatus}!")
    else:
        myjobstatus = False
        print(f"jobstatus: {myjobstatus}!")

name = rand.choice(choices3)
randomnumber = rand.randint(0, 100)
jobstatus = rand.choice(choices4)
function3(name, randomnumber, jobstatus)
name = rand.choice(choices3)
randomnumber = rand.randint(0, 100)
jobstatus = rand.choice(choices4)
function3(name, randomnumber, jobstatus)
name = rand.choice(choices3)
randomnumber = rand.randint(0, 100)
jobstatus = rand.choice(choices4)
function3(name, randomnumber, jobstatus)

print()
print("--------------------")
for i in range(1, 11):
    name = rand.choice(choices3)
    randomnumber = rand.randint(0, 100)
    jobstatus = rand.choice(choices4)
    function3(name, randomnumber, jobstatus)
    print("--------------------")

print()

def function4(name, birthdate, salary):
    print(f"name: {name.capitalize()}!")
    print(f"birthdate: {birthdate}!")
    print(f"salary: ${salary:.2f}!")

name = "panagiwths"
birthdate = dt.datetime(1997, 3, 27)
salary = 1200.555
function4(name, birthdate, salary)

#4:02:50 - https://www.youtube.com/watch?v=ix9cRaBkVe0