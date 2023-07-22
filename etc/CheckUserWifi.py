import platform
import subprocess


def check_wifi_status():
    system = platform.system()
    if system == "Windows":
        return check_wifi_windows()
    elif system == "Darwin":  # macOS
        return check_wifi_mac()
    elif system == "Linux":
        return check_wifi_linux()
    else:
        print("Unsupported operating system.")
        return None


def check_wifi_windows():
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "interface"], universal_newlines=True)
        if "State" in output and "connected" in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return None


def check_wifi_mac():
    try:
        output = subprocess.check_output(
            ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"], universal_newlines=True)
        if "state: running" in output and "status: connected" in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return None


def check_wifi_linux():
    try:
        output = subprocess.check_output(["iwgetid"], universal_newlines=True)
        if "ESSID" in output and "connected" in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return None


if __name__ == "__main__":
    wifi_status = check_wifi_status()
    if wifi_status is None:
        print("Error checking Wi-Fi status.")
    elif wifi_status:
        print("Wi-Fi is connected.")
    else:
        print("Wi-Fi is not connected.")
