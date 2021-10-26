"""
Customer product system that manage customer and product data
<---Starts with the main menu--->
"""

from customer_operations import *
from product_operations import *


def main():
    menu = {'1': "Customer operations.", '2': "Product Operations.", '3': "Queries", '4': "Exit"}
    print()
    print(menu)
    print('------------------------------------------------------------------------------------')

    while True:
        options = menu.keys()
        for entry in options:
            selection = input("Please select from choices above: ")
            if selection == '1':
                print("You are in customer operations!")
                print()
                sub_menu_1 = {'1': "Insert a new customer.",
                              '2': "Delete a customer.",
                              '3': "Update Customer data.",
                              '4': "Write Customer data to a file."}
                while True:
                    options_2 = sub_menu_1.keys()
                    for entry_2 in options_2:
                        print(sub_menu_1)
                        print('---------------------------------------------------------------------------------')
                        selection_2 = input("Please select from choices above: ")
                        if selection_2 == '1':
                            customer_list.append(insert_customer())
                            print(customer_list)

                        elif selection_2 == '2':
                            delete_customer(customer_list)
                            print(customer_list)

                        elif selection_2 == '3':
                            update_customer(customer_list)
                            print(customer_list)

                        elif selection_2 == '4':
                            write_c_data(customer_list)
                            print(customer_list)
                            print()
                            print("Customer information successfully stored.")
                            print()

                        else:
                            print("Unknown Option Selected!")
            elif selection == '2':
                print("You are in product operations.")
                sub_menu_2 = {'1': "Insert a new product.",
                              '2': "Delete a product.",
                              '3': "Update product data.",
                              '4': "Write product data to a file.",
                              '5': "Purchase"}
                while True:
                    options_3 = sub_menu_2.keys()
                    for entry_3 in options_3:
                        print(sub_menu_2)

                        selection_3 = input("Please select: ")
                        if selection_3 == '1':
                            products.append(insert_product())
                            print(products)

                        if selection_3 == '2':
                            delete_product(products)
                            print(products)

                        if selection_3 == '3':
                            update_product(products)
                            print(products)

                        if selection_3 == '4':
                            write_product_data(products)
                            print(products)
                            print("Product data successfully stored!")
                            print()

                        if selection_3 == '5':
                            purchase(products)
                        else:
                            print("Unknown Option Selected!")
            elif selection == '3':
                print("You are in queries section")
                sub_menu_3 = {'1': "Search for a product:",
                              '2': "List the customers",
                              '3': "List the Products",
                              '4': "Quit"}
                while True:
                    options_4 = sub_menu_3.keys()
                    for entry_4 in options_4:
                        print(sub_menu_3)

                        selection_4 = input("Please select:")
                        if selection_4 == '1':
                            search(products)

                        if selection_4 == '2':
                            pass
                        if selection_4 == '3':
                            pass
                        if selection_4 == '4':
                            pass
                        else:
                            print("Unknown Option Selected")

            elif selection == '4':
                break
            else:
                print("Unknown option selected!")


main()
