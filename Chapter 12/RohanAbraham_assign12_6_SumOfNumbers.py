#Rohan Abraham
#Program takes a number and sums up all the numbers that lead up to
#and include it

#Sums up numbers from 0 to n
def sumOfNumbers(n):
    #Stops at 0. Doesn't go into negative numbers
    if n == 0:
        return 0
    #Also accounts for 1 + (1-1)
    elif n == 1:
        return 1
    else:
    #Add the number to the number - 1
    #Very similar to factorial, but uses addition instead of mult
        return n + sumOfNumbers(n-1)

def main():
    #Base case 1
    print(sumOfNumbers(0))
    #Base case 2
    print(sumOfNumbers(1))
    
    print(sumOfNumbers(3))
    
    print(sumOfNumbers(5))

main()
    
