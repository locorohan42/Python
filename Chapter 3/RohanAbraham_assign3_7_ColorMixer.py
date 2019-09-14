#Rohan Abraham
#The user can mix primary colors and the program will display the new color.

color_1 = input("Enter a primary color: ")
color_2 = input("Enter another primary color: ")

if (color_1 == "red" and color_2 == "blue") or (color_2 == "red" and color_1 == "blue"):
    print("You have made purple")
elif (color_1 == "red" and color_2 == "yellow") or (color_2 == "red" and color_1 == "yellow"):
    print("You have made orange")
elif (color_1 == "blue" and color_2 == "yellow") or (color_2 == "blue" and color_1 == "yellow"):
    print("You have made green")
else:
    print("You have entered invalid colors")
