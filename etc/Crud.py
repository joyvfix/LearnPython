# from flask import Flask, render_template, request, redirect
# import sqlite3

# app = Flask(__name__)

# # Create a connection to the SQLite database
# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()

# # Create a table to store users if it doesn't exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         email TEXT NOT NULL
#     )
# ''')
# conn.commit()


# @app.route('/')
# def home():
#     # Fetch all users from the database
#     cursor.execute('SELECT * FROM users')
#     users = cursor.fetchall()
#     return render_template('index.html', users=users)


# @app.route('/add', methods=['GET', 'POST'])
# def add_user():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']

#         # Insert the new user into the database
#         cursor.execute(
#             'INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
#         conn.commit()

#         return redirect('/')
#     return render_template('add.html')


# @app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
# def edit_user(user_id):
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']

#         # Update the user in the database
#         cursor.execute(
#             'UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, user_id))
#         conn.commit()

#         return redirect('/')
#     else:
#         # Fetch the user from the database
#         cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
#         user = cursor.fetchone()
#         return render_template('edit.html', user=user)


# @app.route('/delete/<int:user_id>', methods=['GET', 'POST'])
# def delete_user(user_id):
#     # Delete the user from the database
#     cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
#     conn.commit()

#     return redirect('/')


# if __name__ == '__main__':
#     app.run(debug=True)
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity


# def update_product_price(product, new_price):
#     product.price = new_price


# def update_product_quantity(product, new_quantity):
#     product.quantity = new_quantity


# def delete_product(product_list, product):
#     product_list.remove(product)


# # Create product objects
# product1 = Product("Keyboard", 29.99, 10)
# product2 = Product("Mouse", 14.99, 5)
# product3 = Product("Monitor", 199.99, 3)
# product4 = Product("Headphones", 39.99, 8)

# # Store products in a list
# product_list = [product1, product2, product3, product4]

# # Print product details
# for product in product_list:
#     print("Name:", product.name)
#     print("Price:", product.price)
#     print("Quantity:", product.quantity)
#     print("------------------")

# # Update product price
# update_product_price(product1, 34.99)

# # Update product quantity
# update_product_quantity(product2, 7)

# # Delete product
# delete_product(product_list, product3)

# # Print updated product details
# print("Updated Product List:")
# for product in product_list:
#     print("Name:", product.name)
#     print("Price:", product.price)
#     print("Quantity:", product.quantity)
#     print("------------------")
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class CartItem:
#     def __init__(self, product, quantity):
#         self.product = product
#         self.quantity = quantity

#     def calculate_total(self):
#         return self.product.price * self.quantity


# class Cashier:
#     def __init__(self):
#         self.cart = []

#     def add_item(self, product, quantity):
#         cart_item = CartItem(product, quantity)
#         self.cart.append(cart_item)

#     def remove_item(self, product):
#         for cart_item in self.cart:
#             if cart_item.product == product:
#                 self.cart.remove(cart_item)
#                 break

#     def calculate_total(self):
#         total = 0.0
#         for cart_item in self.cart:
#             total += cart_item.calculate_total()
#         return total

#     def checkout(self, amount_paid):
#         total = self.calculate_total()
#         change = amount_paid - total
#         if change >= 0:
#             self.print_receipt(amount_paid, change)
#         else:
#             print("Insufficient payment. Please provide enough amount.")

#     def print_receipt(self, amount_paid, change):
#         print("=== Receipt ===")
#         for cart_item in self.cart:
#             print(
#                 f"{cart_item.product.name} - Quantity: {cart_item.quantity} - Price: ${cart_item.calculate_total():.2f}")
#         print("----------------")
#         print(f"Total: ${self.calculate_total():.2f}")
#         print(f"Amount Paid: ${amount_paid:.2f}")
#         print(f"Change: ${change:.2f}")


# # Create product objects
# product1 = Product("Keyboard", 29.99)
# product2 = Product("Mouse", 14.99)
# product3 = Product("Monitor", 199.99)

# # Create a Cashier instance
# cashier = Cashier()

# # Add items to the cart
# cashier.add_item(product1, 2)
# cashier.add_item(product2, 3)
# cashier.add_item(product3, 1)

# # Calculate the total
# total = cashier.calculate_total()

# # Process payment
# amount_paid = float(input("Enter amount paid: "))
# cashier.checkout(amount_paid)
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def update_product(self, product_id, name, price):
        product = self.get_product(product_id)
        if product:
            product.name = name
            product.price = price
            return True
        return False

    def delete_product(self, product_id):
        product = self.get_product(product_id)
        if product:
            self.products.remove(product)
            return True
        return False

    def get_all_products(self):
        return self.products


# Create a ProductCatalog instance
catalog = ProductCatalog()


def print_product_details(product):
    print(f"Product ID: {product.id}")
    print(f"Name: {product.name}")
    print(f"Price: ${product.price}")


while True:
    print("Product Management System")
    print("-------------------------")
    print("1. Add Product")
    print("2. View Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        product = Product(id, name, price)
        catalog.add_product(product)
        print("Product added successfully!")
        print("-------------------------")

    elif choice == '2':
        product_id = input("Enter product ID: ")
        product = catalog.get_product(product_id)
        if product:
            print("Product details:")
            print_product_details(product)
        else:
            print("Product not found!")
        print("-------------------------")

    elif choice == '3':
        product_id = input("Enter product ID: ")
        product = catalog.get_product(product_id)
        if product:
            name = input("Enter new product name: ")
            price = float(input("Enter new product price: "))
            if catalog.update_product(product_id, name, price):
                print("Product updated successfully!")
            else:
                print("Failed to update product.")
        else:
            print("Product not found!")
        print("-------------------------")

    elif choice == '4':
        product_id = input("Enter product ID: ")
        product = catalog.get_product(product_id)
        if product:
            if catalog.delete_product(product_id):
                print("Product deleted successfully!")
            else:
                print("Failed to delete product.")
        else:
            print("Product not found!")
        print("-------------------------")

    elif choice == '5':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
        print("-------------------------")
