#Rohan Abraham
#This program has the ChashRegister class

import RetailItem

class CashRegister:
    #Class takes RetailItems
    def __init__(self):
        self.__list = []
        self.__total = 0
        #Initialize the list to empty and the total to zero
    
    def purchase_item(self, RetailItem):
        self.__list.append(RetailItem)
        #Add a RetailItem to the list

    def show_items(self):
        for items in self.__list:
            print(items)
        #Print all of the items in the list

    def get_total(self):
        for items in self.__list:
            self.__total += items.get_price()
        return self.__total
        #Print the total price of the entire list

    def clear(self):
        self.__list = []
        self.__total = 0
        #Clear the list and bring the total back down to zero

    
        
