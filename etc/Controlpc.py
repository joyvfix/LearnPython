import socket
import pyautogui

# Server configuration
HOST = '0.0.0.0'  # Bind to all available interfaces
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening for incoming connections...")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Remote control loop
try:
    while True:
        command = client_socket.recv(1024).decode()
        if not command:
            break

        # Execute remote control commands
        if command == "MOVE_MOUSE":
            x, y = map(int, client_socket.recv(1024).decode().split(","))
            pyautogui.moveTo(x, y)

        elif command == "CLICK":
            pyautogui.click()

        elif command.startswith("TYPE_TEXT"):
            text = command.split(":")[1]
            pyautogui.typewrite(text)

except Exception as e:
    print("Error:", e)

finally:
    client_socket.close()
    server_socket.close()
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}

# Client configuration
HOST = 'REMOTE_PC_IP_ADDRESS'  # Replace with the server's IP address
PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

print("Connected to the remote PC")

# Remote control loop
try:
    while True:
        print("Options:")
        print("1. Move mouse")
        print("2. Click")
        print("3. Type text")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            break

        elif choice == "1":
            x = int(input("Enter x-coordinate: "))
            y = int(input("Enter y-coordinate: "))
            client_socket.sendall(b"MOVE_MOUSE")
            client_socket.sendall(f"{x},{y}".encode())

        elif choice == "2":
            client_socket.sendall(b"CLICK")

        elif choice == "3":
            text = input("Enter the text to type: ")
            client_socket.sendall(f"TYPE_TEXT:{text}".encode())

except Exception as e:
    print("Error:", e)

finally:
    client_socket.close()
