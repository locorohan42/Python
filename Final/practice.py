#Rohan Abraham
#Program takes quiz questions from the jservice api making a quiz with 10 questions from 10 different categories

import requests
import json

RANGE = 10 #Amount of questions wanted
URL = "http://jservice.io/api/random" #API where categories are pulled from

#Create a list without duplicates and if its smaller than 10 call the function again
#Issues with this method?
def Remove(list): 
    new_list = [] 
    for num in list: 
        if num not in new_list: 
            new_list.append(num) 
    return new_list

#If the list without duplicates is smaller than 10 there is definetly an error and it needs to be tried again
def correctCount(list):
    if(len(list) < RANGE):
        getQuestions()
    else:
        return True
    
#Method that calls the api and returns the list of questions and their assocaited values, answers and categories
#Slows things down as api sometimes needs to be called a few times
def getQuestions():
    offset = 0
    category_list = []
    question_list = []
    value_list = []
    answer_list = []

    for i in range(1):
        parameters = {"count" : RANGE, "offset" : offset}
        response = requests.get(URL, params=parameters)
        offset += 100
        j_resp = response.json()

        for i in range (len(j_resp)):
            category = j_resp[i]["category"]["title"]
            question = j_resp[i]["question"]
            value = j_resp[i]["value"]
            answer = j_resp[i]["answer"]
            
            #Lists where values will be stored 
            category_list.append(category)
            question_list.append(question)
            value_list.append(value)
            answer_list.append(answer)

        #Calling all of these creates a new list of categories that does not have any duplicates
        Newlist = Remove(category_list)
        correctCount(Newlist)

        #At this point everything is good and all the arrays can be returned
        return category_list, question_list, value_list, answer_list
        



#Function takes in the list of answers and changes them to make a better user experience
#by removing unnecessary string pieces
def fixAnswers(answer_list):
    newList = []

    for i in range(RANGE):
        if "<i>" or "</i>" or "(" or ")" or "''" in questions[i]:
            answer_list[i] = answer_list[i].replace('""', "")
            answer_list[i] = answer_list[i].replace("<i>", "")
            answer_list[i] = answer_list[i].replace("</i>", "")
            answer_list[i] = answer_list[i].replace("(", "")
            answer_list[i] = answer_list[i].replace(")", "")
            answer_list[i] = answer_list[i].replace("-", "")
            newList.append(answer_list[i])

    return newList

#Function makes dollar values for question 0 if they are not a type
def fixValues(values_list):
    newList = []
    for i in range(RANGE):
        values_list[i] = int(0 if values_list[i] is None else values_list[i])
        newList.append(values_list[i])

    return newList
            
        
            

#Get the lists and store them in lists
categories, questions, values, answers = getQuestions()

#Fix the answers and values.
answers1 = fixAnswers(answers)
values1 = fixValues(values)

#Function where the game is held. Pass the 4 lists of categories, questions, answers and dollar amount for each question
#Function runs through 10 questions keeping track of how how money the user has and prints the amount at the end
def startGame(categories, questions, values1, answers1):
    print("Welcome to Jeopardy.")
    print("We are going to test your knowledge with 10 questions.")
    print()
    userPoints = 0

    for i in range(RANGE):
        print("The category is: " + categories[i])
        print("The question is valued at: $" + str(values1[i]))
        print(questions[i])
        response = input("Enter the answer here: ")
        if(response.upper() == answers1[i].upper()):
            print("Congratulations you got the answer right")
            userPoints += values[i]
            print(values1[i])
            print()
        else:
            print("The correct answer is: " + answers1[i])
            userPoints -= values[i]
            print(values1[i])
            print()
    if(userPoints >= 0):
        print("You have won $" + str(userPoints))
    else:
        print("Yikes. You have lost $" + str(userPoints*-1))

#Function call to start the game
startGame(categories, questions, values1, answers1)

        
            



