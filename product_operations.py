"""
product_operations.py
  <--insertion of a new product-->
  <-- Deletion of a product-->
  <--Updates of product data-->
  <--Writing of product data to a file-->
  <--Purchases-->
"""

PRODUCTS = []
product_file = open("products.txt", "a")


class Product:
    def __init__(self, name, p_id, p_amount, price):
        self.name = name
        self.id = p_id
        self.amount = p_amount
        self.price = price


def insert_product():
    name = input("Enter the product name: ")
    id = input("Enter the product id: ")
    amount = input("Enter the product amount: ")
    price = input("Enter the product price: ")
    product = Product(name, id, amount, price)
    PRODUCTS.append(product)
    print(PRODUCTS)


def delete():
    id_to_delete = input("Enter the product id to delete: ")
    for i in range(len(PRODUCTS)):
        product_id = PRODUCTS[i].id
        if product_id == id_to_delete:
            del PRODUCTS[i]
    print("Product id deleted successfully")


def p_update():
    pass






'''
from customer_operations import *
global customer_id

    
products = [{"name": 'brownies', "product_id": '6749366284624264', "amount": 50, "price": '255.50'},
            {"name": 'cookies', "product_id": '367216784637438', "amount": 90, "price": '100.00'},
            {"name": 'fries', "product_id": '93547264003', "amount": 75, "price": '75.50'}]


def insert_product():
    product_name = input("Enter the product name: ")
    product_amount = int(input("Enter the product amount: "))
    product_price = float(input("Enter the product price: "))
    product_id = id(product_name)
    product_data = {"name": product_name, "product_id": product_id, "amount": product_amount, "price": product_price}
    return product_data


def delete_product(products):
    id_to_delete = input("Enter the product id to delete: ")
    for i in range(len(products) - 1):
        product_id = products[i]['product_id']
        if product_id == id_to_delete:
            products.remove(products[i])
    return products


def update_product(products):
    update_id = input("Enter the product id to update. ")
    print("""
    1. update by name. 
    2. update by price. 
    3. update by amount.""")
    print()
    update_option = int(input("Enter your option from above choices."))
    for i in range(len(products)):
        product_id = products[i]['product_id']
        if product_id == update_id:
            if update_option == 1:
                print("You are about to change product's name! ")
                print()
                new_name = input("Enter new product name: ")
                products[i]['name'] = new_name
            elif update_option == 2:
                print("You are about to change product's price! ")
                print()
                new_price = float(input("Enter new product price: "))
                products[i]['price'] = new_price
            elif update_option == 3:
                print("You are about to change product's amount! ")
                print()
                new_amount = int(input("Enter new product amount: "))
                products[i]['amount'] = new_amount

    return products


def write_product_data(products):
    infile = open("products_data.txt", 'w')
    infile.write(str(products))
    infile.close()


def purchase(products):
    total = 0.0
    customer_id = input("Enter the customer id to purchase: ")
    p_p_id = input("Enter the product id to make a purchase: ")
    purchase_amount = int(input("Enter the amount to purchase: "))
    for i in range(len(products)):
        if p_p_id == products[i]['product_id']:
            if purchase_amount <= products[i]['amount']:
                amount = products[i]['amount'] - purchase_amount
                products[i]['amount'] = amount
                purchased = products[i]['name']
                price = products[i]['price']
                price = float(price)
                spent = price * amount
                total = total + spent
                details = {"customer id": customer_id, "amount purchased": purchase_amount,
                           "purchased": purchased, "total spent": total}
                print("Purchase done successfully and details stored!")
                #writing to a file
                infile = open("purchase_details.txt", "w")
                infile.write(str(details))
                infile.close()
            else:
                print("Out of stock.")



"""
<---QUERIES SECTION--->
   -search of a product
   -listing of all customers
   -listing of products
   -list customer's name, products bought and total amount spent
   -quit
"""


def search(products):
    p_search = input("Enter the product id to search: ")
    for i in range(len(products)):
        if p_search == products[i]['product_id']:
            amount = products[i]['amount']
            price = products[i]['price']
            print("product found: ", products[i]['name'], "\namount is:", amount, "\nPrice is: ", price)
            break
        else:
            print("Product not found! ")


def list_products_and_customers():
    option = int(input("What would you like to list?\n 1.Customers\n2.Products\nChoose option from above:"))
    if option == 1:
        write_c_data(customer_list)
        c_list = open("Customers.txt", "r").read()
        print(c_list)
    elif option == 2:
        write_product_data(products)
        p_list = open("products_data.txt", "r").read()
        print(p_list)


def customer_details():
    customerDetails = open("purchase_details.txt", "r").read()
    print(customerDetails)
'''






