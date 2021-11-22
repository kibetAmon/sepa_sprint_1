"""
Customer product system that manage customer and product data
<---Starts with the main menu--->
"""

from customer_operations import *
from product_operations import *


def main_menu():
    print("""
                            WELCOME TO NAIVAS >>>>>>>>>>>>>
                            GROCERY SHOPPING MADE EASY!!!!!
                            
    Please proceed to main menu below to chose your operation.
    """)
    print("....................................................................................")
    Exit = True

    while Exit == True:

        print("""
                           1. Customer Operations
                           2. Product Operations
                           3. Queries
                           4. Exit
                           """)
        selection = int(input("Please select from the main menu above the operation to perform:"))
        print("-------------------------------------------------------------------------------")
        if selection == 1:
            print("You are in customer operations!")
            customer_menu()
        elif selection == 2:
            print("You are in Product Operations")
            product_menu()
        elif selection == 3:
            print("You are in Queries section")
            queries_menu()
        else:
            Exit = False



main_menu()
customer_file()
