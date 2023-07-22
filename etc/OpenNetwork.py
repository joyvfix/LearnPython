import subprocess


def create_open_wifi_ssid(ssid):
    config = f"""
    interface=wlan0
    ssid={ssid}
    hw_mode=g
    channel=7
    macaddr_acl=0
    auth_algs=1
    ignore_broadcast_ssid=0
    """
    try:
        with open("/tmp/hostapd.conf", "w") as f:
            f.write(config)

        subprocess.run("sudo ifconfig wlan0 up", shell=True)
        subprocess.run("sudo hostapd /tmp/hostapd.conf", shell=True)
        print(f"Wi-Fi hotspot '{ssid}' created successfully.")
    except subprocess.CalledProcessError:
        print("Error creating Wi-Fi hotspot.")


if __name__ == "__main__":
    wifi_ssid = "MyOpenWiFi"
    create_open_wifi_ssid(wifi_ssid)
