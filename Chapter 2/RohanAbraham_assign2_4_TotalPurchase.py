item_one = int(input("Enter the price of the first item"))
item_two = int(input("Enter the price of the second item"))
item_three = int(input("Enter the price of the third item"))
item_four = int(input("Enter the price of the fourth item"))
item_five = int(input("Enter the price of the fifth item"))

print("")

sub_total = item_one + item_two + item_three + item_four + item_five
sales_tax = 0.07
total = sub_total + sub_total * sales_tax

print("The subtotal of the sale is $",sub_total)
print("The sales tax is", format(sales_tax, "0.0%"))
print("With tax included the total comes down to $",total) 

