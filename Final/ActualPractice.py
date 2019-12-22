thislist = ["apple", "banana", "cherry", "pear", "mango", "coconut", "booty",
            "meat", "squirrel", "pikachu"]
print(len(thislist))

def correctCount(list):
    if(len(list) < 10):
        print("what a fail")
    else:
        print("good length")

correctCount(thislist)

a = "a!b@c#d$"
b = "!@#$"
for char in b:
    a = a.replace(char,"") 

print(a)
