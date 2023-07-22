
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# kasir sederhana
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# def tampilkan_menu():
#     print("========== MENU ==========")
#     print("1. Tambahkan item")
#     print("2. Hapus item")
#     print("3. Tampilkan total")
#     print("4. Keluar")
#     print("==========================")


# def tambahkan_item(keranjang):
#     item = input("Masukkan nama item: ")
#     harga = float(input("Masukkan harga item: "))
#     keranjang[item] = harga
#     print("Item berhasil ditambahkan!")


# def hapus_item(keranjang):
#     item = input("Masukkan nama item yang akan dihapus: ")
#     if item in keranjang:
#         del keranjang[item]
#         print("Item berhasil dihapus!")
#     else:
#         print("Item tidak ditemukan dalam keranjang.")


# def tampilkan_total(keranjang):
#     total = sum(keranjang.values())
#     print("Total harga: $", total)


# keranjang = {}

# while True:
#     tampilkan_menu()
#     pilihan = input("Pilih menu (1-4): ")

#     if pilihan == "1":
#         tambahkan_item(keranjang)
#     elif pilihan == "2":
#         hapus_item(keranjang)
#     elif pilihan == "3":
#         tampilkan_total(keranjang)
#     elif pilihan == "4":
#         print("Terima kasih!")
#         break
#     else:
#         print("Pilihan tidak valid. Silakan pilih menu 1-4.")
#  {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# calculator
#  {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# def add(num1, num2):
#     return num1 + num2


# def subtract(num1, num2):
#     return num1 - num2


# def multiply(num1, num2):
#     return num1 * num2


# def divide(num1, num2):
#     if num2 != 0:
#         return num1 / num2
#     else:
#         return "Error: Cannot divide by zero"


# print("Simple Calculator")
# print("-----------------")

# while True:
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     choice = input("Enter choice (1-5): ")

#     if choice == '5':
#         print("Calculator has been terminated.")
#         break

#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if choice == '1':
#         result = add(num1, num2)
#         print("Result: ", result)
#     elif choice == '2':
#         result = subtract(num1, num2)
#         print("Result: ", result)
#     elif choice == '3':
#         result = multiply(num1, num2)
#         print("Result: ", result)
#     elif choice == '4':
#         result = divide(num1, num2)
#         print("Result: ", result)
#     else:
#         print("Invalid input. Please try again.")
# (;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;)
# (;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_total(self):
        return self.product.price * self.quantity


class Checkout:
    def __init__(self):
        self.cart = []

    def add_item(self, product, quantity):
        cart_item = CartItem(product, quantity)
        self.cart.append(cart_item)

    def remove_item(self, product):
        for cart_item in self.cart:
            if cart_item.product == product:
                self.cart.remove(cart_item)
                break

    def calculate_total(self):
        total = 0.0
        for cart_item in self.cart:
            total += cart_item.calculate_total()
        return total

    def print_receipt(self):
        print("=== Receipt ===")
        for cart_item in self.cart:
            print(
                f"{cart_item.product.name} - Quantity: {cart_item.quantity} - Price: ${cart_item.calculate_total():.2f}")
        print("----------------")
        print(f"Total: ${self.calculate_total():.2f}")


# Create product objects
product1 = Product("Keyboard", 29.99)
product2 = Product("Mouse", 14.99)
product3 = Product("Monitor", 199.99)

# Create a checkout instance
checkout = Checkout()

# Add items to the cart
checkout.add_item(product1, 2)
checkout.add_item(product2, 3)
checkout.add_item(product3, 1)

# Print the receipt
checkout.print_receipt()

# Remove an item from the cart
checkout.remove_item(product2)

# Print the updated receipt
checkout.print_receipt()
