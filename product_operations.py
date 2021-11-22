"""
product_operations.py
  <--insertion of a new product-->
  <-- Deletion of a product-->
  <--Updates of product data-->
  <--Writing of product data to a file-->
  <--Purchases-->
"""

PRODUCTS = []


class Product:
    def __init__(self, name, p_id, amount, price):
        self.name = name
        self.p_id = p_id
        self.amount = amount
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount


def insert_product():
    name = input("Enter the product name: ")
    p_id = input("Enter the product id: ")
    amount = int(input("Enter the product amount: "))
    price = float(input("Enter the product price: "))
    product = Product(name, p_id, amount, price)
    PRODUCTS.append(product)
    print("Product inserted successfully and stored in the file")
    products_file()


def delete():
    load_product()
    id_to_delete = input("Enter the product id to delete: ")
    for i in range(len(PRODUCTS)-1):
        if PRODUCTS[i].p_id == id_to_delete:
            del PRODUCTS[i]
            print("Product successfully deleted")
        else:
            print("Invalid ID")
            break
    products_file()


def p_update():
    load_product()
    update_id = input("Enter the product id to update. ")
    print("""
        1. update by name. 
        2. update by price. 
        3. update by amount.""")
    print()
    update_option = int(input("Enter your option from above choices."))
    for i in range(len(PRODUCTS)-1):
        if PRODUCTS[i].p_id == update_id:
            if update_option == 1:
                name = input("Enter new product name: ")
                PRODUCTS[i].set_name(name)
                print("Updated the name to:", PRODUCTS[i].get_name())
                break
            elif update_option == 2:
                price = float(input("Enter a new price"))
                PRODUCTS[i].set_price(price)
                print("Updated the price to: ", PRODUCTS[i].get_price())
                break
            else:
                amount = input("Enter a new amount")
                PRODUCTS[i].set_amount(amount)
                print("Updated the amount to: ", PRODUCTS[i].get_amount())
                break
        else:
            print("Invalid id")
            break
    products_file()


def products_file():
    with open('products.txt', "w") as myfile:
        for pr in PRODUCTS:
            print(pr.name, pr.p_id, pr.amount, pr.price, file=myfile)
            break


def load_product():
    product = open("products.txt", "r")
    for p in product:
        pr = p.split(" ")
        name = pr[0]
        p_id = pr[1]
        amount = int(pr[2])
        price = pr[3]
        product = Product(name, p_id, amount, price)
        PRODUCTS.append(product)


def purchase():
    load_product()
    total = 0.0
    customer_id = input("Enter the customer id to purchase: ")
    p_p_id = input("Enter the product id to make a purchase: ")
    purchase_amount = int(input("Enter the amount to purchase: "))
    for i in range(len(PRODUCTS)):
        if p_p_id == PRODUCTS[i].p_id:
            if PRODUCTS[i].amount >= purchase_amount:
                PRODUCTS[i].set_amount(PRODUCTS[i].amount - purchase_amount)
                PRODUCTS[i].get_amount()

                remaining = PRODUCTS[i].amount - purchase_amount
                PRODUCTS[i].set_amount(remaining)
                PRODUCTS[i].get_amount()

                purchased = PRODUCTS[i].name
                price = float(PRODUCTS[i].price)
                spent = price * purchase_amount
                total = total + spent
                details = {"customer id": customer_id, "amount purchased": purchase_amount,
                           "purchased": purchased, "total spent": total}
                print("Purchase done successfully and details stored!")
                # writing to a file
                infile = open("purchase_details.txt", "w")
                infile.write(str(details))
                infile.close()
                break
            else:
                print("Out of stock.")




'''
<---QUERIES SECTION--->
   -search of a product
   -listing of all customers
   -listing of products
   -list customer's name, products bought and total amount spent
   -quit
'''


def search():
    load_product()
    search_id = input("Enter the product id to search: ")
    for i in range(len(PRODUCTS)):
        if search_id == PRODUCTS[i].p_id:
            for Product in PRODUCTS:
                print("Product found is: ")
                print(Product.name, Product.p_id, Product.amount, Product.price)
                break
        else:
            print("Invalid Id entered")


def list_products_and_customers():
    option = int(input("What would you like to list?\n 1.Customers\n2.Products\nChoose option from above:"))
    if option == 1:
        c_list = open("customer.txt", "r").read()
        print(c_list)
    elif option == 2:
        p_list = open("products.txt", "r").read()
        print(p_list)


def customer_details():
    details = open("purchase_details.txt", "r").read()
    print(details)


def product_menu():
    Exit = True

    while Exit == True:
        print("""
                1. Insert a new Product
                2. Delete a Product
                3. Update Product data
                4. Purchase
                5. Back to main
                """)
        selection = int(input("Please select a product operation from choices above: "))
        if selection == 1:
            insert_product()
            print("---------------------------")
            proceed = int(input("\nPress 1 to continue inserting and 2 for the menu: "))
            if proceed == 1:
                insert_product()
                print("----------------------")
                product_menu()
            else:
                product_menu()

        elif selection == 2:
            delete()
            print("-----------------------------")
            proceed = int(input("Press 1 to continue deleting and 2 for the menu"))
            if proceed == 1:
                delete()
                print("-------------------------")
                product_menu()
            else:
                product_menu()

        elif selection == 3:
            p_update()
            print("------------------------------")
            proceed = int(input("Press 1 to continue updating and 2 for the menu"))
            if proceed == 1:
                p_update()
                print("---------------------------")
                product_menu()
            else:
                product_menu()
        elif selection == 4:
            purchase()
            print("--------------------------------")
            proceed = int(input("Press 1 to continue purchasing or 2 for the menu"))
            if proceed == 1:
                purchase()
                break
            else:
                product_menu()
        else:
            Exit = False


def queries_menu():
    Exit = True

    while Exit == True:
        print("""
            1. Search for a Product
            2. List Customers and Products
            3. List Customer's purchase details
            4. Back to main
            """)

        selection = int(input("Please select a query operation from above choices:"))
        if selection == 1:
            search()
            print("--------------------------")
            proceed = int(input("Would you like to proceed to: \n1.List customers and products"
                                "\n2. Go to menu \nEnter Here: "))
            if proceed == 1:
                list_products_and_customers()
                print("----------------------")
                queries_menu()
            else:
                queries_menu()

        elif selection == 2:
            list_products_and_customers()
            print("-------------------------")
            proceed = int(input("Would you like to proceed to: \n1.List customer's purchase details "
                                "2.Go to the menu \nEnter Here: "))
            if proceed == 1:
                customer_details()
                print("-------------------")
                queries_menu()
            else:
                queries_menu()

        elif selection == 3:
            customer_details()
            print("---------------------------------------------------")
        else:
            Exit = False