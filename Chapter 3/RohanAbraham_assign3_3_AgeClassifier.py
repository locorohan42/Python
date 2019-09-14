#Rohan Abraham
#Program will classify the user according to their age.

age = int(input("Pleas enter your age"))
if age <= 1:
    print("You are an infant")
elif age > 1 and age < 13:
    print("You are a child")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20:
    print("You are and adult")
else:
    print("You enterered an invalid value! Try again...")
