#Rohan Abraham
#Program writes random numbers to a file and reads and displays the file later
import random

def main():
    def FileWriter():
        try:
            #Get user input 
            num_of_random_numbers = int(input("How many random numbers do you want written to the file? "))
            #Open file for writing
            number_file = open('numbers.txt', 'w')

            #Store random numbers in the file
            for count in range(0, num_of_random_numbers):
                number = random.randint(1, 500)
                number_file.write(str(number) + '\n')
    
    
            number_file.close()
            print('Data written to numbers.txt'+'\n')

        except IOError:
            print("An error while reading the file")

        except ValueError:
            print("Non-numeric data found in the file")

        except:
            print("An error occured")

    def FileReader():
        try:
            number_file = open('numbers.txt', 'r')
            line = number_file.readline()
            count = 0
            total = 0
            print("Numbers that were added: \n")
            while line != "":
                amount = int(line)
                print(amount)
                total+=amount
                line = number_file.readline()
                count += 1
            

            print(str(count) + " Numbers were added")
            print("The total of the numbers is: " + str(total))
            number_file.close()
            
        except IOError:
            print("An error while reading the file")

        except ValueError:
            print("Non-numeric data found in the file")

        except:
            print("An error occured")

    FileWriter()
    FileReader()


main()

