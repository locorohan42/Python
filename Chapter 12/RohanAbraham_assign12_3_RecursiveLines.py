#Rohan Abraham
#Program prints asterisks line by line with the number of asterisks increasing
#by one for each line

#method prints lines of asterisks
def lines(n):
    #When n is one just print one asterisk
    if n == 1:
        print("*")
    #Otherwise decrement n and print n asterisks
    #Takes advantage of string multiplaction
    else:
        lines(n-1)
        print("*"*n)
        
        
       

def main():
    #Base case
    lines(1)
    print()
    lines(3)
    print()
    lines(5)
   
main()
