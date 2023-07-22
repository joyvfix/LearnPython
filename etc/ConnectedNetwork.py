import psutil


def check_connected_network():
    interfaces = psutil.net_if_stats()

    for interface, stats in interfaces.items():
        if stats.isup and not stats.isloopback:
            addresses = psutil.net_if_addrs().get(interface, [])
            for address in addresses:
                if address.family == psutil.AF_INET:
                    return interface, address.address

    return None


if __name__ == "__main__":
    network_info = check_connected_network()
    if network_info:
        interface_name, ip_address = network_info
        print(f"Connected network: {interface_name}")
        print(f"IP Address: {ip_address}")
    else:
        print("No active network connection.")
