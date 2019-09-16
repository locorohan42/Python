#Rohan Abraham
#Program models the growth of a population based on inputs from the user

amount_of_organisms = int(input("Starting number of organisms: "))
amount_of_increase = int(input("Average daily increase: "))
amount_of_days = int(input("Number of days to multiply: "))
day = 1

print("Day approximate \t Population")
for i in range(amount_of_days):
    print(str(day) +"        \t    \t " + str(amount_of_organisms))
    day+=1
    amount_of_organisms = amount_of_organisms + amount_of_organisms*(amount_of_increase/100)

