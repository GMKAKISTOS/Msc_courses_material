import time

from classinfo import classinfo
from classinfo import classinfo2
from classinfo import classinfo5
import datetime as dt

if __name__ == "__main__":
    myinfo2 = classinfo("nikos", "georgopoulos", 30, 2550.50)
    print()
    print(myinfo2)
    myinfo3 = classinfo()
    print()
    print(myinfo3)
    myinfo2.firstname = "alexis"
    myinfo2.salary = 1175.25
    print()
    print(myinfo2)
    print()
    myinfo2.coststatus()
    myinfo3.coststatus()
    myinfo2.salary = 10000
    myinfo2.coststatus()
    myinfo3.salary = 20000
    myinfo3.coststatus()

    print()
    test1 = classinfo2()
    test1.test()
    print(test1)

    print()
    test5 = classinfo5()
    test5.test2()
    test5.test3()
    test5.test4()
    print(test5)

    print()
    test6 = classinfo2()
    print(test6)
    test6.jobstatus = False
    test6.salary = 3000
    print()
    print(test6)

    print()
    test7 = classinfo("foivos", "giannopoulos", 35)
    print(test7)

    print()
    start = time.time()
    for i in range(1, 11):
        #time.sleep(3)
        print(i, end = " ")
    end = time.time()
    print()
    print(end - start)

print()
try:
    while True:
        number = float(input("enter a number: "))
        if(number == 10):
            break
        else:
            continue
except ValueError:
    print("not a number!")
finally:
    print("some things happening!")
    number = 20
    print(f"number: {number}!")

#8:48:29 - https://www.youtube.com/watch?v=ix9cRaBkVe0


