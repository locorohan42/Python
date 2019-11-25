#! python3
import re
print("Let's find out how often your favorite singers say I or you!")
singer = input("Enter the name of a singer: ")
word = input("Enter a word to be searched for: ")

batRegex = re.compile(word)
def createFileName(singer):
    String = r"C:\Users\Locoroho97\PythonFiles\MyPythonScripts\ " + singer.lower() + ".txt"
    return String.replace(" ", "")
#C:\Users\Locoroho97\PythonFiles\Chapter 2\mac.txt
#C:\Users\Locoroho97\PythonFiles\MyPythonScripts\asap.txt
filePath = createFileName(singer)
print(filePath)
def fileRead(filePath):
    with open(filePath, 'r') as file:
        return file.read().replace('\n', '')

data = fileRead(filePath)
mo = batRegex.findall(data)
print(singer + " likes saying " + word + " In 4 of his top songs he says it " +str(len(mo)) + " times." )
print()
