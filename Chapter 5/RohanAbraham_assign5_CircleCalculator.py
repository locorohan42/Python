#Rohan Abraham
#Circle Calculator
from math import pi
def compute_area(radius):
    return radius**2 * pi

def compute_perimeter(radius):
    return radius * pi * 2

def compute_diameter(radius):
    return radius * 2


def main():

    print("Circle Calculator")

    radius = float(input("Enter the radius: "))

    print("Would you like Area, Perimeter or Diameter?")
    print("Enter: ")
    print("   A for area")
    print("   P for perimeter")
    print("   D for diameter")
    choice = input("Your choice: ")

    if(choice == "A" or choice == "a"):
        area = compute_area(radius)
        print("The area is: ", area)
    elif(choice == "P" or choice == "p"):
        perimeter = compute_perimeter(radius)
        print("The perimeter is: ", perimeter)
    elif(choice == "D" or choice == "d"):
        diameter = compute_diameter(radius)
        print("The diameter is: ", diameter)
    else:
        print("An error occured. Try again")

main()
    
