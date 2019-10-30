#Rohan Abraham
#Simple Poker Game

import random
def main():
    
    deck = []
    for i in range(4):
        card = 1
        for i in range(13):
            deck.append(card)
            card += 1

    random.shuffle(deck)

    num_of_cards = int(input("Enter the number of cards desired: "))
    player_1_hand = []
    player_2_hand = []
    card_index = 0
    player_1_score = 0
    player_2_score = 0

    
    #Add cards to the player 1 deck and increments their score
    for i in range(num_of_cards):
            player_1_hand.append(deck[card_index])
            player_1_score += deck[card_index]
            card_index+=1

    #Ensure the hand doesn't exceed 26
    #If the hand was more than 26, cards are repeatedly removed to
    #be in accordance with the rules
    while(player_1_score > 26):
        player_1_score-=player_1_hand[-1]
        del player_1_hand[-1]
        card_index-=1

    for i in range(num_of_cards):
        player_2_hand.append(deck[card_index])
        player_2_score += deck[card_index]
        card_index+=1
            
    while(player_2_score > 26):
        player_2_score-=player_2_hand[-1]
        del player_2_hand[-1]
        card_index-=1
              
    print("player 1 hand: " + str(player_1_hand))
    print("player 1 score: " + str(player_1_score))
    print()
    print("player 2 hand: " + str(player_2_hand))
    print("player 2 score: " + str(player_2_score))
    print()

    if(player_1_score > player_2_score):
        print("Player 1 has won")
    elif(player_2_score > player_1_score):
        print("Player 2 has won")
    else:
        print("There has been a tie")

    
   
 
main()
