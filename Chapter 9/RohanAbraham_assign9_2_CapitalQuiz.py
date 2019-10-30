#Rohan Abraham
#Program acts as a quiz to test the users knowledge of capitals or year
#of statehood

#Function reads a file and makes a dictionary
#Takes the filename and increment value to ensure that two
#Dictionaries can be created
def file_read(filename, inc):
    #Open file for reading
    file = open(filename, 'r')

    #Read in the words, get rid of \n and \t so that
    #words can easily be split by |
    text1 = file.read()
    text1 = text1.replace("\n", "|")
    text1 = text1.replace("\t", "")
    word_list1 = text1.split("|")

    #Helps correct for case sensitiveness for the quiz
    for word1 in word_list1:
            word_1 = ""
            for i in range(len(word1)):
                word_1 += word1[i].lower()
                
            word_list1[word_list1.index(word1)] = word_1
       
    #create an empty dictionary
    #state name will be key
    #Increment parameter will decide if the value is the year or capital
    state1 = {}
    for num in range(0, len(word_list1)-2, 4):
        state1[word_list1[num]] = word_list1[num+2+inc]

        
    #File closed and the dictionary is returned
    file.close()
    return state1

#Function takes user input for which game to start by taking a dictionary also a name which lets the user know if they should
#Enter a capital or statehood year
def start_game(dict, name):
    #Initilaize score and compare the guess to the value
    #If the guess is correct the score increments
    #The key refers to the state
    score = 0     
    for i in range(10):
        key, value = dict.popitem()
        guess = input("Enter the " +  name + " " + key + " ")
        if(guess.lower() == value):
            score +=1
    #Prints answers right using score, abs needed for answers wrong and multiply by a float to get the percentage    
    print("You got " + str(score) + " answers right")
    print("You got " + str(abs(score-10)) + " answers wrong")
    print("Your percentage is " + str(score*10.0) + "%") 


def main(): 
    years = file_read("StateList.txt", 0)
    capitals = file_read("StateList.txt", 1)

    print("Would you like the capitals or year of statehood quiz?")
    user_input = int(input("Enter 1 for years or 2 for capitals: "))            
                          
    if (user_input == 1):
        dict = years
        name = "statehood year"
    else:
        dict = capitals
        name = "capital"

    start_game(dict, name)
        
    
main()
