#Rohan Abraham
#Program takes a list of books and reads/writes the list to JSON

import json

#Function takes in four values and assings keys to each value
#Returns a dictionary for a book
def make_book(isbn, name, author, format, pages):
    dict = {
        "ISBN" : isbn,
        "name" : name,
        "author" : author,
        "format" : format,
        "pages" : pages
    }
    return dict



#Function takes a list of books and writes the JSON version to a file
def save_catalog(list_of_books):
    list = json.dumps(list_of_books)
    with open('catalog.json', 'w') as file:
        file.write(list)
        file.close()



#Function loads the contents of a json file and prints it to the screen
def read_catalog(file_name):
    file = json.load(open(file_name))
    return file



def main():
    #Add some initial data for testing 
    book0 = make_book("978-1338299144", "Harry Potter and the Socerer's Stone", "JK Rowling",
        "paperback", 336)
    book1 = make_book("978-0134444321", "Starting Out with Python", "Tony Gaddis",
        "paperback", 722)
    book2 = make_book("978-0321992789", "Programming: Principles and Practice Using C++", "Bjarne Stroustrup",
        "paperback", 1312)
    book3 = make_book("978-0131103627", "C Programming Language", "Kernighan and Ritchie",
        "paperback", 272)

    books = []
    books.insert(0, book0)
    books.insert(1, book1)
    books.insert(2, book2)
    books.insert(3, book3)
    
    save_catalog(books)
    
    #Assignment requirements
    map = read_catalog('catalog.json')
    print(map)
    print()

    prompt = ""
    while prompt != 'n':
        i = 4
        prompt = input("Would you like to add a book?\ny for yes n for no ")
        if(prompt != 'n'):
            
            field0 = input("Enter the isbn: ")
            field1 = input("Enter the name: ")
            field2 = input("Enter the author: ")
            field3 = input("Enter the format: ")
            field4 = input("Enter the number of pages: ")
            book = make_book(field0, field1, field2, field3, field4)
            books.insert(i, book)
            i += 1
            
    print("Thanks for adding some books")
    save_catalog(books)
    
    

main()
