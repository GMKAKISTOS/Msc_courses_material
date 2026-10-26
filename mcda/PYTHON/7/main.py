import random as rand

#3:19:42 - https://www.youtube.com/watch?v=ix9cRaBkVe0

print()
randomnumber = rand.randint(0, 100)

print(f"random number: {randomnumber}")

status = "third age!" if randomnumber >= 70 else "second age!" if randomnumber > 50 and randomnumber < 70 else "first age!"
print(f"status: {status}")

