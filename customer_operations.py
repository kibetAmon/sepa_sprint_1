"""
Customer_operations.py
    <--insertion of new customers-->
    <--deletion of customers-->
    <--updating customers-->
    <--writing of customer data to a file-->
"""


global customer_id

def insert_customer():
    customer_name = input("Enter a customer name: ")
    customer_id = input("Enter the customer Id: ")
    customer_address = input("Enter the customer address: ")
    customer_data = [customer_name, customer_id, customer_address]
    return customer_data


def delete_customer():
    id_to_delete = int(input("Enter the customer id to delete: "))
    customer_id = insert_customer()
    if id_to_delete == customer_id:
        del id_to_delete


def update_customer():
    update_data = int(input("Enter the customer id: "))
    if update_data != "":
        insert_customer()



def write_data():
    customer_data = insert_customer()
    infile = open('Customers.txt', 'w')
    infile.write(str(customer_data))
    infile.close()



delete_customer()
