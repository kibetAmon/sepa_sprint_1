"""
Customer_operations.py
    <--insertion of new customers-->
    <--deletion of customers-->
    <--updating customers-->
    <--writing of customer data to a file-->
"""

customer_list = [{"name": 'amon', "address": '20400', "customer_id": '140734621121696'},
                 {"name": 'Felix', "address": '50100', "customer_id": '140734621121728'},
                 {"name": 'Jeremy', "address": '56700', "customer_id": '140734617124064'}]


def insert_customer():
    customer_name = input("Enter a customer name: ")
    customer_address = input("Enter the customer address: ")
    customer_id = id(customer_name)
    customer_data = [customer_name, customer_id, customer_address]
    return customer_data


def delete_customer(customer_list):
    id_to_delete = int(input("Enter the customer id to delete: "))
    for i in range(len(customer_list)-1):
        customer_id = customer_list[i]['customer_id']
        if customer_id == id_to_delete:
            customer_list.remove(customer_list[i])
    return customer_list


def update_customer():
    update_data = int(input("Enter the customer id: "))
    if update_data != "":
        insert_customer()


def write_data():
    customer_data = insert_customer()
    infile = open('Customers.txt', 'w')
    infile.write(str(customer_data))
    infile.close()


delete_customer(customer_list)