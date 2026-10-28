import time

def function1(name = "panos" , age = 29, salary = 1200):
    print(f"name: {name}, age: {age}, salary: {salary}")

print()
print("----------")
function1()
print("----------")
function1("giwrgos", 30, 1100)
print("----------")
function1("nikolaos", 31)
print("----------")
function1("antreas")

print()
start = time.time()
for i in range(1, 11):
    #time.sleep(2)
    print(i, end = " ")
end = time.time()

seconds = end - start
print(f"total time: {seconds} seconds!")
minutes = (end - start) / 60
print(f"total time: {minutes} minutes!")
hours = (end - start) / 3600
print(f"total time: {hours} hours!")

print()
print("----------")
function1( salary = 1300, age = 25)
print("----------")
function1(age = 26, name = "kwstas")
print("----------")
function1(salary = 4000, name = "kwstas")
print("----------")
function1(salary = 3000)
print("----------")
function1(age = 20)

print()
def function2(*args, **kwargs):
    print(args)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

function2(10, "kwstas", age = 20, name = "kwstas")

print()
evennumbers = [ x if x % 2 == 0 else "noteven" for x in range(0, 11)]
print(evennumbers)
evennumbers.clear()
evennumbers = [x for x in range(0, 11) if x % 2 == 0]
print(evennumbers)
evennumbers.clear()
evennumbers = [x * 3 for x in range(0, 11)]
print(evennumbers)
numbers = [-20, 35, -25, 30, 500, -200, 100, -43]
notnegativenumbers = [x for x in numbers if x > 0]
print(notnegativenumbers)
notnegativenumbers.sort()
print(notnegativenumbers)
