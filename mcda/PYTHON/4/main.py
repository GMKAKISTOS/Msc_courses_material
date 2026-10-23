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