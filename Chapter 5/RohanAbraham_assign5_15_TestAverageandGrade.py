#Rohan Abraham
#Program takes five test scores from user input and outputs a letter grade for
#each score and the average of the test scores

print("Enter Five test scores: \n")

test1 = int(input("Test 1: "))
test2 = int(input("Test 2: "))
test3 = int(input("Test 3: "))
test4 = int(input("Test 4: "))
test5 = int(input("Test 5: "))

def determine_grade(test):
    if(test>=90):
        return "You got an A"
    elif(test >= 80 and test <= 89):
        return "You got a B"
    elif(test >=70 and test <=79):
        return "You got a C"
    elif(test >=60 and test <=69):
        return "You got a D"
    else:
        return "You got an F"

def calc_average(test1, test2, test3, test4, test5):
    return (test1+test2+test3+test4+test5)/5

average = calc_average(test1, test2, test3, test4, test5)

print("")
print("Test 1 Grade: " + str(determine_grade(test1)))
print("Test 2 Grade: " + str(determine_grade(test2)))
print("Test 3 Grade: " + str(determine_grade(test3)))
print("Test 4 Grade: " + str(determine_grade(test4)))
print("Test 5 Grade: " + str(determine_grade(test5)))

print("Your testing average is: " + str(average))


