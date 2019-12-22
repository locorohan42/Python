#Rohan Abraham
#Program uses recursion to determine wheather or not a
#string is a palindrome

#Method takes a string and an index that starts at 0
#After calling function prints wheather the inputted string is a
#palindrome or not
i = 0
def palindrome(string):
    #Base case when the string is empty
    if(string == ""):
        return "This is a palindrome."
    #Will compare the front and back of a string until it is empty
    if(string[i] == string[-1]):
        return palindrome(string[i+1:-1])

    #Code executes when it is not a palindrome
    return "This is not a palindrome. Good try."

def print_encjdkf(text, offset):
    print(text

def main():
    #Base case
    print(palindrome(""))
    print(palindrome("able was i ere i saw elba"))
    print(palindrome("racecar"))
    #Fail test
    print(palindrome("hiho"))

main()
