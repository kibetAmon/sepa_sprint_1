"""
Customer product system that manage customer and product data
<---Starts with the main menu--->
"""

from customer_operations import *
from product_operations import *


def main():
    print("""
    Welcome to Drip lab. Your best choice of amazing kicks !
    Please proceed to main menu below to chose your operation.
    """)
    print("..................................................")

    while True:
        selection = int(input("Please select from the main menu below the operation to perform:"
                              " \n1. Customer Operations \n2. Product Operation \n3.Queries"
                              "\nEnter Your Choice Here:  "))
        print("-------------------------------------------------------------------------------")
        if selection == 1:
            print("You are in customer operations!")
            print()
            print("""
                1. Insert a new Customer
                2. Delete a Customer
                3. Update a Customer
                4. Write Customer data to a file
                """)
            while True:
                print('---------------------------------------------------------------------------------')
                selection_2 = int(input("Please select from customer operations above: "))
                if selection_2 == 1:
                    insert_customer()
                    print("Customer inserted successfully.")
                    print("-----------------------------")
                    proceed = int(input("Would you like to: \n 1.Delete a customer  2.Exit \nEnter Here: "))
                    if proceed == 1:
                        delete_customer()
                        print("Customer deleted successfully")
                        print("-------------------------")
                        break
                    else:
                        exit()

                elif selection_2 == 2:
                    delete_customer()
                    print("Customer deleted successfully")
                    print("-----------------------------")
                    proceed = int(input("Would you like to: \n1. Update a customer 2. Exit \nEnter Here: "))
                    if proceed == 1:
                        update_customer()
                        print(CUSTOMERS, "\nCustomer information successfully updated.")
                        print("------------------------")
                        break
                    else:
                        exit()


                elif selection_2 == 3:
                    update_customer()
                    print("Customer information successfully updated.")
                    print("----------------------------")
                    proceed = int(input("Would you like to: \n1. Write customer data to a file 2. Exit \nEnter Here"))
                    if proceed == 1:
                        write_file()
                        print("Customer information successfully stored.")
                        print("-----------------------")
                        break
                    else:
                        exit()


                elif selection_2 == 4:
                    write_file()
                    print("Customer information successfully stored.")
                    print("-----------------------------")
                    proceed = int(input("Would you like to : \n1. Proceed to Product operations 2. Exit \nEnter Here:"))
                    if proceed == 1:
                        print("""
                        Kindly Choose Option 2 from the main menu
                        """)
                        main()
                    else:
                        exit()

                else:
                    main()



'''
        elif selection == 2:
            print("You are in product operations.")
            print()
            print("""
                1. Insert a new Product
                2. Delete a Product
                3. Update Product data
                4. Write Product data to a file
                5. Purchase
                """)
            while True:
                selection_3 = int(input("Please select a product operation from choices above: "))
                if selection_3 == 1:
                    products.append(insert_product())
                    print(products, "\nNew Product inserted successfully.")
                    print("---------------------------")
                    proceed = int(input("Would you like to: \n1.Delete a Product 2. Exit \nEnter Here:"))
                    if proceed == 1:
                        delete_product(products)
                        print(products, "\nProduct deleted Successfully! ")
                        print("----------------------")
                        break
                    else:
                        exit()

                elif selection_3 == 2:
                    delete_product(products)
                    print(products, "\nProduct deleted Successfully! ")
                    print("-----------------------------")
                    proceed = int(input("Would you like to: \n1. Update product info 2. Exit \nEnter Here:"))
                    if proceed == 1:
                        update_product(products)
                        print(products, "\nProduct updated successfully.")
                        print("-------------------------")
                        break
                    else:
                        exit()

                elif selection_3 == 3:
                    update_product(products)
                    print(products, "\nProduct updated successfully.")
                    print("------------------------------")
                    proceed = int(input("Would you like to: \n1. Store product info 2. Exit \nEnter Here:"))
                    if proceed == 1:
                        write_product_data(products)
                        print(products, "\nProduct data successfully stored!")
                        print("---------------------------")
                        break
                    else:
                        exit()
                elif selection_3 == 4:
                    write_product_data(products)
                    print(products, "\nProduct data successfully stored!")
                    print("------------------------------")
                    proceed = int(input("Would you like to: \n1. Purchase 2. Exit \nEnter Here: "))
                    if proceed == 1:
                        purchase(products)
                        print("---------------------------")
                        break
                    else:
                        exit()
                elif selection_3 == 5:
                    purchase(products)
                    print("--------------------------------")
                    proceed = int(input("Would you like to: \n1. Proceed to queries 2.Exit \nEnter Here:"))
                    if proceed == 1:
                        print("""
                        Kindly choose option 3 in the main menu
                        """)
                        main()
                    else:
                        exit()
                else:
                    print("Unknown Option Selected!")
                    main()
        elif selection == 3:
            print("You are in queries section")
            print()
            print("""
                1. Search for a Product
                2. List Customers and Products
                3. List Customer's purchase details
                """)
            while True:
                selection_4 = int(input("Please select:"))
                if selection_4 == 1:
                    search(products)
                    print("--------------------------")
                    proceed = int(input("Would you like to proceed to: \n1.List customers and products"
                                        "2. Exit \nEnter Here: "))
                    if proceed == 1:
                        list_products_and_customers()
                        break
                    else:
                        exit()

                elif selection_4 == 2:
                    list_products_and_customers()
                    print("-------------------------")
                    proceed = int(input("Would you like to proceed to: \n1.List customer's purchase details"
                                        "2. Exit \nEnter Here"))
                    if proceed == 1:
                        customer_details()
                        break
                    else:
                        exit()

                elif selection_4 == 3:
                    customer_details()
                    print("---------------------------------------------------")
                    out = int(input("Done with operations! \nWould you like to: 1. Exit 2.Proceed to main menu"
                                    "\nEnter Here: "))
                    if out == 1:
                        exit()
                    else:
                        print("""
                        WELCOME BACK!!
                        """)
                        print("<<<<<<<<<<<<>>>>>>>>>>>")
                        main()


                else:
                    print("Unknown Option Selected")
                    main()
        else:
            print("""
            Unknown Option Selected! \nChoose option number 1, 2 or 3
            """)
            print("---------------------")

'''
main()
