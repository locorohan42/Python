num_of_cookies = int(input("How many cookies do you want to make?"))

cups_of_sugar = 1.5
cup_of_butter = 1.0
cups_of_flower = 1.75

amount_of_sugar = num_of_cookies * cups_of_sugar / 48
amount_of_butter = num_of_cookies * cup_of_butter / 48
amount_of_flower = num_of_cookies * cups_of_flower / 48

print("For", num_of_cookies, "cookies you will need: ")

print(format(amount_of_sugar, ',.2f') + " cups of sugar")
print(format(amount_of_butter, ',.2f') + " cups of butter")
print(format(amount_of_flower, ',.2f') + " cups of flower")


print("Happy Baking!")
