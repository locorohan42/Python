#Rohan Abraham
#Program will roll the dice 100 times and average the value of the die
#The user gets to choose how many sides the dice has
import random



print("Dice Roller\n")

number_of_dice = int(input("Enter the number of dice: "))
while(number_of_dice < 1):
    print("Enter a valid number of dice")
    number_of_dice = int(input("Enter the number of dice: "))
   
    
    
number_of_sides = int(input("Enter the number of sides each dice will have: "))
while(number_of_sides < 2):
    print("Enter a valid number of sides")
    number_of_sides = int(input("Enter the number of sides each dice will have: "))
    
    
def calculate_lower_limit(dice):
    return dice
def calculate_upper_limit(dice, sides):
    return dice * sides

lower_limit = calculate_lower_limit(number_of_dice)
upper_llimit = calculate_upper_limit(number_of_dice, number_of_sides)
runningTotal = 0

for i in range(100):
    number = random.randint(lower_limit, upper_llimit)
    runningTotal+=number
   

average = runningTotal/100
print("The average roll was " + str(average))



