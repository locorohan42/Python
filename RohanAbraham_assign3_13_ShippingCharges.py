#Rohan Abraham
#Program will calculate the cost of shipping for a given weight.

weight = int(input("Enter the weight of the package"))

if(weight <= 2):
    print("Shipping charge of $1.50")
elif(weight > 2 and weight <= 6):
    print("Shipping charge of $3.00")
elif(weight > 6 and weight <=10 ):
    print("Shipping charge of $4.00")
elif(weight > 10):
    print("Shipping charge of $4.75")
else:
    print("An error occured. Try again")
