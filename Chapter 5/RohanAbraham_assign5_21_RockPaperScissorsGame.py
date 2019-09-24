#Rohan Abraham
#Program is a rock paper scissors game where the user plays a computer
import random

randomNumber = random.randrange(1,4)
randomValue = "Potential"

if(randomNumber == 1):
    randomValue = "rock"
elif(randomNumber == 2):
    randomValue = "paper"
else:
    randomValue = "scissors"
  
user_choice = input("Enter rock, paper or scissors: ")
print("The computer chose " + randomValue)
    

def choose_winner(user, robot):
    if(user == robot):
        print("There is a tie. Play again")
    elif(user == "rock" and robot == "scissors"):
         print("The player won!")
    elif(user == "scissors" and robot == "paper"):
          print("The player won!")
    elif(user == "paper" and robot == "rock"):
           print("The player won!")
    elif(robot == "rock" and user == "scissors"):
         print("The computer won!")
    elif(robot == "scissors" and user == "paper"):
          print("The computer won!")
    elif(robot == "paper" and user == "rock"):
           print("The computer won!")
    else:
        print("an error occured")

gameOutput = choose_winner(user_choice, randomValue)
print(gameOutput)
