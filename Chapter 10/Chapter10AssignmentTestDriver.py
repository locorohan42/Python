#Rohan Abraham
#This program is a testing method for the RetailItem and CashRegister classes
import RetailItem
import CashRegister
import random



def test():
    #Test the retail item class works
    print("*******Retail Item test*******")
    my_item = RetailItem.RetailItem("Jacket", 12, 59.95)
    my_item2 = RetailItem.RetailItem("Designer Jeans", 40, 34.95)
    my_item3 = RetailItem.RetailItem("Shirt", 20, 24.95)
    print("Item #1 ", my_item)
    print("Item #2 ", my_item2)
    print("Item #3 ", my_item3)
    print()

    #test with one item
    print("*******Cash Register Tests*******")
    print("*******One item*******")
    my_item3 = RetailItem.RetailItem("Designer Jeans", 40, random.uniform(35.5,100.5))
    my_item4 = RetailItem.RetailItem("Shirt", 20, random.uniform(10.5,50.5))
    my_item5 = RetailItem.RetailItem("Hat", 26, random.uniform(10.5,30.5))
    my_item6 = RetailItem.RetailItem("Backpack", 55, random.uniform(20.5,80.5))
    my_item7 = RetailItem.RetailItem("Jacket", 39, random.uniform(40.5,130.5))
    my_register = CashRegister.CashRegister()
    my_register.purchase_item(my_item)
    my_register.show_items()
    print("Total price: $" + "%.2f" % my_register.get_total())
    print()

    #Test with no items
    print("*******Zero Items*******")
    my_register.clear()
    my_register.show_items()
    print("Total price: $" + "%.2f" % my_register.get_total())
    print()

    #Test with multiple items
    print("*******Multiple Items*******")
    my_register.purchase_item(my_item7)
    my_register.purchase_item(my_item3)
    my_register.purchase_item(my_item4)
    my_register.purchase_item(my_item5)
    my_register.purchase_item(my_item6)
    my_register.show_items()
    print("Total price: $" + "%.2f" % my_register.get_total())
    print()

test()
