"""
Customer product system that manage customer and product data
<---Starts with the main menu--->
"""

from customer_operations import *
from product_operations import *


def main():
    print("""
        1. Customer Operations
        2. Product Operations
        3. Queries
    """)
    print()
    print('------------------------------------------------------------------------------------')

    while True:
        selection = int(input("Please select from the menu above: "))
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
                        customer_list.append(insert_customer())
                        print(customer_list, "\nCustomer inserted successfully.")

                    elif selection_2 == 2:
                        delete_customer(customer_list)
                        print(customer_list, "\nCustomer deleted successfully")

                    elif selection_2 == 3:
                        update_customer(customer_list)
                        print(customer_list, "\nCustomer information successfully updated.")

                    elif selection_2 == 4:
                        write_c_data(customer_list)
                        print(customer_list, "\nCustomer information successfully stored.")
                        print()

                    else:
                        print("Unknown Option Selected!")

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
                elif selection_3 == 2:
                    delete_product(products)
                    print(products, "\nProduct deleted Successfully! ")
                elif selection_3 == 4:
                    update_product(products)
                    print(products, "\nProduct updated successfully.")
                elif selection_3 == 4:
                    write_product_data(products)
                    print(products, "\nProduct data successfully stored!")
                    print()
                elif selection_3 == 5:
                    purchase(products)
                else:
                    print("Unknown Option Selected!")
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

                elif selection_4 == 2:
                    list_products_and_customers()
                    break

                elif selection_4 == 3:
                    pass

                else:
                    print("Unknown Option Selected")
        elif selection == '4':
                break


main()
