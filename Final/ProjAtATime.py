#Rohan Abraham
#Program takes quiz questions from the jservice api making a quiz with 10 different categories

import requests
import json

#Create a list without duplicates and if its smaller than 10 call the function again
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

#If the list without duplicates is smaller than 10 there is definetly an error and it needs to be tried again
def correctCount(list):
    if(len(list) < 10):
        getCategories()
    else:
        return True
    
def getCategories():
    url = "http://jservice.io/api/random"
    offset = 0

    category_list = []

    #while True:
    for i in range(1):
        parameters = {"count" : 10, "offset" : offset}
        #Change how the parameters works ugh
        response = requests.get(url, params=parameters)
        offset += 100
        j_resp = response.json()
        
       # if (len(j_resp) < 1):
       #    break
        
        for i in range (len(j_resp)):
            cat_id = j_resp[i]["id"]
            title = j_resp[i]["question"]
            #print(title, cat_id)
            print(cat_id)

            #Array where things will be stored to make sure there are no duplicate categories
            category_list.append(cat_id)
            
        for x in category_list:
            print(x)

        Remove(category_list)
        print(len(category_list))
        correctCount(category_list)
        

getCategories()
             
        #Store the 10 categories in an array and if there are duplicates just call the api again for all of them
        #Store the questions and answers in an array and prompt the user to answer ignoring
