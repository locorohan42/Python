#Rohan Abraham
#Program outputs the power of a number using recursion

#Function takes an integer n and raises to a power that is the
#exponent parameter
def power(n, exponent):
    #Added precondtion to help debugging 
    if(exponent < 0):
        return "Please enter a positive exponent value"
    #N to the 0 is always 1
    elif(exponent == 0):
        return 1
    #N to the 1 is always just n
    elif(exponent == 1):
        return n
    #Otherwise n will multiply itself exp times
    else:
        return n * power(n, exponent-1)

def main():
    #Precondtion test
    print(power(5,-1))
    #Base case 1
    print(power(5,0))
    #Base case 2
    print(power(5,1))
    print(power(5,3))
    print(power(2,4))
    

main()
