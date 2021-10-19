"""
product_operations.py
  <--insertion of a new product-->
  <-- Deletion of a product-->
  <--Updates of product data-->
  <--Writing of product data to a file-->
  <--Purchases-->
"""

products = [{"name": 'brownies', "id": '6749366284624264', "amount": 50, "price": '255.50'},
            {"name": 'cookies', "id": '367216784637438', "amount": 90, "price": '100.00'},
            {"name": 'fries', "id": '93547264003', "amount": 75, "price": '75.50'}]


def insert_product():
    product_name = input("Enter the product name: ")
    product_amount = int(input("Enter the product amount: "))
    product_price = float(input("Enter the product price: "))
    product_id = id(product_name)


def delete_product():
    pass


def Update_product():
    pass


def write_product():
    pass


def purchase():
    pass
