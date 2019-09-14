#Rohan Abraham
#Program asks the user for a number of days and each day they get one penny
#then the amount of pennies each doubles each day accumulting over time

amount_of_days = int(input("Enter the amount of days: \n"))
total_pennies = 0
penny = 1
day = 1
dollar = penny/100

for i in range(amount_of_days):
  
        
        #Just for fun if statements make numbers properly align 
        total_pennies+= dollar
        if(day < 10):
            print("Day   "+ str(day) +"  : $" + str(dollar))
            day+=1
            dollar = dollar * 2
        elif(day < 100):
            print("Day   "+ str(day) +" : $" + str(dollar))
            day+=1
            dollar = dollar * 2
        else:
            print("Day   "+ str(day) +": $" + str(dollar))
            day+=1
            dollar = dollar * 2
    

print("\nTotal salary is $",format(total_pennies,',.2f'), sep ='')
    

