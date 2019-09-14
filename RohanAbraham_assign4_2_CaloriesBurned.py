#Rohan Abraham
#Caluculates calories burned on the treadmill for a certain time
#10, 15, 20, 25 and 30 minutes

calories_per_minute = 4.2

print("Calories burned for 10, 15, 20, 25 and 30 minutes: " + "\n")
for i in range(10, 31, 5):
    print("Calories Burned: " + str(calories_per_minute * i))
