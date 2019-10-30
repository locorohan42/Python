#Rohan Abraham
#Lets the uers input a name of a team and then displays the amount of times
#that team has won the World Series

def main():
    win_count = 0
    team = input("Enter the name of a team: ")
    
    infile = open('WorldSeriesWinners.txt', 'r')

    winners = infile.readlines()

    index = 0
    while index < len(winners):
        winners[index] = winners[index].rstrip('\n')
        index+=1

    

    for i in range(len(winners)):
        if winners[i] == team:
            win_count += 1

    print("From 1903 through 2009 the " + team + " has won " + str(win_count) + " times.")
 
main()
