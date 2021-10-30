"""
product_operations.py
  <--insertion of a new product-->
  <-- Deletion of a product-->
  <--Updates of product data-->
  <--Writing of product data to a file-->
  <--Purchases-->
"""

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
    customer_id = input("Enter the customer id to purchase: ")
    p_p_id = input("Enter the product id to make a purchase: ")
    purchase_amount = int(input("Enter the amount to purchase: "))
    for i in range(len(products)):
        if p_p_id == products[i]['product_id']:
            if purchase_amount <= products[i]['amount']:
                amount = products[i]['amount'] - purchase_amount
                products[i]['amount'] = amount
            else:
                print("Out of stock.")

    print("\nCustomer Id is: ", customer_id, "\nProduct Id is: ",
          p_p_id, "\nAmount purchased is: ", purchase_amount, "\nRemaining amount is: ", amount)


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


def customer_details(products, customer_list):
    for i in range(len(customer_list)):
        name = customer_list[i]['name']
        print(name)



