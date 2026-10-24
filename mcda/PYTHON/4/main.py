firstName = "panagiwths"
lastName = "xronopoylos"
fullName = firstName + " " + lastName
print()
print(firstName + " - " + str(len(firstName)))
print(lastName + " - " + str(len(lastName)))
print(fullName + " - " + str(len(fullName)))
exists1 = fullName.find(" ")
exists2 = True if exists1 != -1 else False
print(f"index number : {exists1} - exists? : {exists2}")
exists1 = fullName.find("o")
exists2 = True if exists1 != -1 else False
print(f"index number : {exists1} - exists? : {exists2}")
exists1 = fullName.rfind("o")
exists2 = True if exists1 != -1 else False
print(f"index number : {exists1} - exists? : {exists2}")
exists1 = fullName.find("o", 14)
exists2 = True if exists1 != -1 else False
print(f"index number : {exists1} - exists? : {exists2}")
firstName = firstName.capitalize()
lastName = lastName.capitalize()
fullName = firstName + " " + lastName
print(fullName)
fullName = fullName.lower()
print(fullName)
fullName = fullName.upper()
print(fullName)
fullName = fullName[0:1].upper() + fullName[1:10].lower() + fullName[10:11] + fullName[11:12].upper() + fullName[12:].lower()
print(fullName)
trueorfalse = fullName.isalpha()
print(f"{fullName} - {trueorfalse}")
fullName = fullName[0:1] + fullName[1:10] + fullName[10:11].strip() + fullName[11:12] + fullName[12:]
trueorfalse = fullName.isalpha()
print(f"{fullName} - {trueorfalse}")
trueorfalse = fullName.isdigit()
print(trueorfalse)
fullName = fullName[0:1].upper() + fullName[1:10].lower() + fullName[10:11].upper() + fullName[11:].lower()
trueorfalse = fullName.isalpha()
print(f"{fullName} - {trueorfalse}")
fullName = fullName[0:1] + fullName[1:10] + " " + fullName[10:11] + fullName[11:]
print(fullName)
kena = fullName.count(" ")
print(kena)
fullName = fullName.replace(" ", "-")
print(fullName)
kena = fullName.count(" ")
print(kena)

#1:39:08 - https://www.youtube.com/watch?v=ix9cRaBkVe0

print()
name = "panos"
pos = name.index("s", 0, len(name))
print(f"Position: {pos}")
creditcardnumber = "1234-5678-9101112"
print(f"credit card number: {creditcardnumber}")
print(creditcardnumber[0:4])
print(creditcardnumber[5:9])
print(creditcardnumber[10:])
print(creditcardnumber[0:4] + creditcardnumber[5:9] + creditcardnumber[10:])
print(creditcardnumber[0:4] + "-" + creditcardnumber[5:9] + "-" + creditcardnumber[10:])
name = "nikos"
print(name[0::1])
print(name[0::2])
print(name[0::3])
print(name[0::4])
print(name[0::5])
print(name[0:len(name):2])
print(name[2::])
print(name[:-2])
print(creditcardnumber[len(creditcardnumber) - 4:])
print(creditcardnumber[-len(creditcardnumber) + ((len(creditcardnumber)) - 4):])
print(creditcardnumber[-4:])
print(creditcardnumber[::-1])
print(creditcardnumber[-1:-len(creditcardnumber)-1:-1])

print()
j = 3.12345
print(f"{j:.2f}")
print(f"{j:.3f}")
j = -13.451
print(f"{j:.2f}")
print(f"{j:.3f}")
print(f"{j:.4f}")
print(f"{j:10}")#ten spaces
print(f"{j:010}")
print(f"{j:<10}")
print(f"{j:>10}")
print(f"{j:^10}")
j = 13.451
print(f"{j:+}")
print(f"{j: }")
j = -13.451
print(f"{j:-}")
j = 13000.14
print(f"{j:,}")
print(f"{j:+,.2f}")

#1:51:55 - https://www.youtube.com/watch?v=ix9cRaBkVe0