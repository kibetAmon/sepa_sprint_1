"""
Customer_operations.py
    <--insertion of new customers-->
    <--deletion of customers-->
    <--updating customers-->
    <--writing of customer data to a file-->
"""

CUSTOMERS = []


class Customers:
    def __init__(self, name, c_id, address):
        self.name = name
        self.c_id = c_id
        self.address = address

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address


def insert_customer():
    name = input("Enter a customer's name: ")
    c_id = input("Enter a customer's id: ")
    address = input("Enter a customer's address: ")
    customer = Customers(name, c_id, address)
    CUSTOMERS.append(customer)
    print("customer inserted successfully and details stored.")
    customer_file()


def delete_customer():
    load_customer()
    cus_id = input("Enter the customer id to delete: ")
    for i in range(len(CUSTOMERS)-1):
        if CUSTOMERS[i].c_id == cus_id:
            del CUSTOMERS[i]
            print("Customer deleted successfully")
        else:
            print("Invalid ID")
            break

    customer_file()


def update_customer():
    load_customer()
    update_id = input("Kindly enter the customer id to update: ")
    print("""
    1. update by name.
    2. update by address.""")
    update_option = int(input("Enter your update option: "))
    for i in range(len(CUSTOMERS)-1):
        if CUSTOMERS[i].c_id == update_id:
            if update_option == 1:
                name = input("Enter a new name: ")
                CUSTOMERS[i].set_name(name)
                print("updated name to: ", CUSTOMERS[i].get_name())
            else:
                address = input("Enter a new address")
                CUSTOMERS[i].set_address(address)
                print("Updated the address to:", CUSTOMERS[i].get_address())
        else:
            print("Invalid Id")
            break
    customer_file()


def customer_file():
    with open('customer.txt', "w") as myfile:
        for c in CUSTOMERS:
            print(c.name, c.c_id, c.address, file=myfile)
            break


def load_customer():
    customer = open("customer.txt", "r")
    for c in customer:
        cst = c.split(" ")
        #print(cst)
        name = cst[0]
        c_id = cst[1]
        address = cst[2]
        customer = Customers(name, c_id, address)
        CUSTOMERS.append(customer)


def customer_menu():
    Exit = True

    while Exit == True:
        print("""
     1. Insert a new Customer
     2. Delete a Customer
     3. Update a Customer
     4. Back to main
    """)

        print('---------------------------------------------------------------------------------')
        selection = int(input("Please select from customer operations above: "))

        if selection == 1:
            insert_customer()
            print("-----------------------------")
            proceed = int(input("\nPress 1 to continue inserting and 2 for the the menu: "))
            if proceed == 1:
                insert_customer()
                customer_file()
                print("-------------------------")
                customer_menu()
            else:
                customer_menu()

        elif selection == 2:
            delete_customer()
            print("-----------------------------")
            proceed = int(input("\nPress 1 to continue deleting and 2 for the menu: "))
            if proceed == 1:
                delete_customer()
                print("------------------------")
                customer_menu()
            else:
                customer_menu()

        elif selection == 3:
            update_customer()
            print("----------------------------")
            proceed = int(input("press 1 to continue updating and 2 for the menu"))
            if proceed == 1:
                update_customer()
                print("-----------------------")
                customer_menu()
            else:
                customer_menu()

        else:
            Exit = False