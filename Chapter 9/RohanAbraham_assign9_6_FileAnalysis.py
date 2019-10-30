#Rohan Abraham
#Program analyzes two files finding unique words, words that appear in both files,
#Words that are in the first and not the second and visa versa and words
#that are in a file, but not both files


#The set of words that are in both files
def union(set1, set2):
    return set1.union(set2)

#Set of words in the first, but not the second
def first_not_second(set1, set2):
    return set1.difference(set2)

#Set of words in the second, but not the first
def second_not_first(set1, set2):
    return set2.difference(set1)

#Set of words that are in one set, but not both
def not_both(set1, set2):
    return set1.symmetric_difference(set2)

def unique_set(filename):
    #Start by opening the file
    file = open(filename, 'r')

    #Some marks aren't needed and will make a word include a symbol at the end
    text1 = file.read()
    text1 = text1.replace("\n", " ")
    text1 = text1.replace(";", " ")
    text1 = text1.replace(",", " ")
    text1 = text1.replace(".", " ")
    text1 = text1.replace("!", " ")

    #List can be split by spaces
    word_list1 = text1.split(" ")

    #Whitespace may splip in as well as letter in the second set
    word_set = set(word_list1)
    word_set.discard("")
    word_set.discard("T")
    word_set.discard("A")
    word_set.discard("C")
    word_set.discard("G")

    #Close file and return the set
    file.close()
    return word_set


def main():
    word_set1 = unique_set("VeryModelOfAScientistSalarian.txt")
    word_set = unique_set('VeryModelOfAModernMajor-General.txt')
    
    union1 = union(word_set, word_set1)

    first_not_second1 = first_not_second(word_set, word_set1)
                           
    second_not_first1 = second_not_first(word_set, word_set1)

    not_both1 = not_both(word_set, word_set1)

    print("The unique words in the first set")
    print(word_set)
    print("")

    print("The unique words in the second set ")
    print(word_set1)
    print("")

    print("The words in the intersection set: ")
    print(union1)
    print("")

    print("The words in the first_not_second set: ")
    print(first_not_second1)
    print("")

    print("The words in the second_not_first set: ")
    print(second_not_first1)
    print("")

    print("The words in the not_both set: ")
    print(not_both1)
    print("")
   

    



main()
