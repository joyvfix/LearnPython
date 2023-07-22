import socket


def check_wifi_status():
    host = "8.8.8.8"  # Google's public DNS server
    port = 53  # DNS port

    try:
        # Set the timeout for the connection attempt
        socket.setdefaulttimeout(5)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False


if __name__ == "__main__":
    wifi_status = check_wifi_status()
    if wifi_status:
        print("Wi-Fi is connected.")
    else:
        print("Wi-Fi is not connected.")
