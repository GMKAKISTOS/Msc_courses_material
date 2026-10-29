from classinfo import classinfo
from classinfo import classinfo2

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

#7:00:03 - https://www.youtube.com/watch?v=ix9cRaBkVe0



