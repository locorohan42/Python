#Rohan Abraham
#Program displays the average rainfall over a period of years

amount_of_years = int(input("Enter the amount of years: "))
months = 0
total_rainfall = 0

for i in range(amount_of_years):
    for i in range(12):
        amount_of_rainfall = int(input("Enter the amount of rainfall for the month (in inches): "))
        total_rainfall+=amount_of_rainfall
        months+=1

print("")
print("Amount of Months: " + str(months))
print("Total amount of inches of rain: " + str(total_rainfall))
print("Average rainfall per month: " + str(total_rainfall/months))
        
