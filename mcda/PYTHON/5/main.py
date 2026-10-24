#1:51:55 - https://www.youtube.com/watch?v=ix9cRaBkVe0

i = 1
while i <= 10:
    if(i != 10):
        if (i == 1):
            print()
            print(i, end = " ")
        else:
            print(i, end = " ")
    else:
        print(i, end = "")
        print()
    i = i + 1

i = 1
status = True
while status:
    if(i == 10):
        print(i, end = "")
    else:
        if(i == 1):
            print()
            print(i, end = " ")
        else:
            print(i, end = " ")
    i = i + 1
    if( i == 11):
        print()
        status = False
