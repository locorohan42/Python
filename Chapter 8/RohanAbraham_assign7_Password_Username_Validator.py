#Rohan Abraham
#Password Validator
import time

def main():
    
    #Function makes sure password does not contain obvious phrases
    #The in operator determines if a certain string is in the password
    #All functions write to file and return False in case of an error otherwise return True
    #Functions return true or False to be used as flags to deterimine if error code 0 is present or not
    def obviousPassword(password, username):
        if 'password' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif '1234' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
            
        
        elif '111111' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'Qwerty123' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'Abcd1234' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'football' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'dragon' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'letmein' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'iloveyou' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'admin' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'login' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'welcome' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'flower' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'zaq1' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        elif 'Password1' in password:
            print("Don't use common passwords")
            file = open('errorResults.txt','a')
            file.write("Obvious Password(Error Code 10)      ")
            file.close()
            return False
        
        else:
            return True
       

    #Fucntion makes sure the password is at least 8 characaters long      
    def tooShortPassword(password, username):
        if(len(password) < 8):
            print("Password must be at least 8 characters long")
            file = open('errorResults.txt','a')
            file.write("Too Short Password (Error Code 20)" +"\t")
            file.close()
            return False
        else:
            return True
       
            
            
    #Function makes sure password has a lowercase char, uppercase char and a digit
    def lowComplexityPassword(password, username):
        #Flags are initilized to False
        has_uppercase = False
        has_lowercase = False
        has_digit = False
        
        #For loop goes through the password checking if the password has the required fields
        for letter in password:
            if letter.isupper():
               has_uppercase = True
            if letter.islower():
                has_lowercase = True
            if letter.isdigit():
                has_digit = True

        #At the end if statement looks to see if any flags were raised
        if(has_uppercase == False or has_lowercase == False or has_digit == False):
            print("Passwords must contain both upper and lower case letters and at least one digit")
            file = open('errorResults.txt','a')
            file.write("Low Complexity Password (Error Code 30)" + "      ")
            file.close()
            return False
        else:
            return True

    #Checks if password is the same as username or spelled backwards or contains username
    def otherProblems(password, username):

        #Calls the reverse helper method to keep the method neat and clean
        if(password.upper() == reverse(username).upper()):
            print("Passwords can't contain a variation of the username")
            file = open('errorResults.txt','a')
            file.write("Other Problems (Error Code 99)" + "      ")
            file.close()
            return False
        elif(password.upper() == username.upper()):
            print("Passwords can't contain a variation of the username")
            file = open('errorResults.txt','a')
            file.write("Other Problems (Error Code 99)" + "      ")
            file.close()
            return False
        elif(password.upper() in username.upper()):
            print("Passwords can't contain a variation of the username")
            file = open('errorResults.txt','a')
            file.write("Other Problems (Error Code 99)" + "      ")
            file.close()
            return False
        else:
            return True
        

    #Helper method for otherProblems(). Returns a reversed string   
    def reverse(string):
        #Starts at the end of the string and goes back to the beginning one at a time
        reversed_name = string[len(string)::-1]
        return reversed_name

    #Last functions that uses a flag to see if any other error were raised
    #Methods will be called and the result of True or False will be stored in flags
    #Had to use 6 spaces instead of a tab since it was being written as one space instead of a tab in most spots
    def validPassword(flag1, flag2, flag3, flag4):
        if flag1 == True and flag2 == True and flag3 == True and flag4 == True:
            print("You have a good password!")
            file = open('errorResults.txt','a')
            file.write("Valid Password (Error Code 0)" + "      " + name + "      " + time.ctime() + "\n")
            file.close()
        else:
            print("Invalid Password")
            file = open('errorResults.txt','a')
            file.write(name + "      " + time.ctime() + "\n")
            file.close()

    #Loop allows input for 10 times     
    count = 0   
    while(count < 10):
        file = open('errorResults.txt','a')
        name = str(input('enter username'))
        password = str(input('enter password'))
        flag1 = obviousPassword(password, name)
        flag2 = tooShortPassword(password, name)
        flag3 = lowComplexityPassword(password, name)
        flag4 = otherProblems(password, name)
        validPassword(flag1, flag2, flag3, flag4)
        file.close()
        count += 1

   
    
   
 
main()
