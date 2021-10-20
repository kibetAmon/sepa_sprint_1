"""
product_operations.py
  <--insertion of a new product-->
  <-- Deletion of a product-->
  <--Updates of product data-->
  <--Writing of product data to a file-->
  <--Purchases-->
"""

products = [{"name": 'brownies', "product_id": '6749366284624264', "amount": 50, "price": '255.50'},
            {"name": 'cookies', "product_id": '367216784637438', "amount": 90, "price": '100.00'},
            {"name": 'fries', "product_id": '93547264003', "amount": 75, "price": '75.50'}]


def insert_product():
    product_name = input("Enter the product name: ")
    product_amount = int(input("Enter the product amount: "))
    product_price = float(input("Enter the product price: "))
    product_id = id(product_name)
    product_data = [product_name, product_id, product_amount, product_price]
    return product_data


def delete_product(products):
    id_to_delete = input("Enter the product id to delete: ")
    for i in range(len(products) - 1):
        product_id = products[i]['product_id']
        if product_id == id_to_delete:
            products.remove(products[i])
    return products


def Update_product():
    pass


def write_product():
    pass


def purchase():
    pass
