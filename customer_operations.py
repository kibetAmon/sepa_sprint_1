"""
Customer_operations.py
    <--insertion of new customers-->
    <--deletion of customers-->
    <--updating customers-->
    <--writing of customer data to a file-->
"""

CUSTOMERS = []
Customer_file = open("customer.txt", "a")


class Customers:
    def __init__(self, name, address, c_id):
        self.name = name
        self.address = address
        self.c_id = c_id


def insert_customer():
    name = input("Enter a customer's name: ")
    c_id = input("Enter a customer's id: ")
    address = input("Enter a customer's address: ")
    customer = Customers(name, c_id, address)
    CUSTOMERS.append(customer)
    return CUSTOMERS


def delete_customer():
    cus_id = input("Enter the customer id to delete")
    for i in range(len(CUSTOMERS)):
        customer_id = CUSTOMERS[i].c_id
        if customer_id == cus_id:
            del CUSTOMERS[i]
    print("Customer deleted successfully")


def update_customer():
    update_id = input("Kindly enter the customer id to update: ")
    print("""
    1. update by name.
    2. update by address.""")
    update_option = int(input("Enter your update option: "))
    for i in range(len(CUSTOMERS)):
        c_id = CUSTOMERS[i].c_id
        if c_id == update_id:
            if update_option == 1:
                new_name = input("Enter a new name")
                CUSTOMERS.name = new_name
            else:
                new_address = input("Enter a new address")
                CUSTOMERS.address = new_address
                break
    return CUSTOMERS


def write_file():
    print(CUSTOMERS, file = Customer_file)



'''
customer_list = [{"name": 'amon', "address": '20400', "customer_id": '140734621121696'},
                 {"name": 'Felix', "address": '50100', "customer_id": '140734621121728'},
                 {"name": 'Jeremy', "address": '56700', "customer_id": '140734617124064'}]


def insert_customer():
    customer_name = input("Enter a customer name: ")
    customer_address = input("Enter the customer address: ")
    customer_id = id(customer_name)
    customer_data = {"name": customer_name, "address": customer_address, "customer_id": customer_id}
    return customer_data


def delete_customer(customer_list):
    id_to_delete = input("Enter the customer id to delete: ")
    for i in range(len(customer_list) - 1):
        customer_id = customer_list[i]['customer_id']
        if customer_id == id_to_delete:
            customer_list.remove(customer_list[i])
    return customer_list


def update_customer(customer_list):
    update_id = input("Kindly enter the customer id to update: ")
    print("""
    1. update by name.
    2. update by address.""")
    print()
    update_option = int(input("Enter your option from above: "))
    for i in range(len(customer_list)):
        customer_id = customer_list[i]['customer_id']
        if customer_id == update_id:
            if update_option == 1:
                print("You are about to change a customer's name!")
                print()
                new_name = input("Enter a new name: ")
                customer_list[i]['name'] = new_name
            elif update_option == 2:
                print("You are about to change a customer's address! ")
                print()
                new_address = input("Enter a new address: ")
                customer_list[i]['address'] = new_address
    return customer_list


def write_c_data(customer_list):
    infile = open('Customers.txt', 'w')
    infile.write(str(customer_list))
    infile.close()
'''

insert_customer()