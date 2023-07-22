import os
import platform
import subprocess


def sleep_or_shutdown(action):
    system = platform.system()

    if system == "Windows":
        if action == "sleep":
            # Put the computer to sleep
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif action == "shutdown":
            # Initiate a shutdown
            os.system("shutdown /s /t 0")
        else:
            print("Invalid action specified.")
    elif system == "Linux" or system == "Darwin":
        if action == "sleep":
            # Put the computer to sleep
            subprocess.run(["systemctl", "suspend"])
        elif action == "shutdown":
            # Initiate a shutdown
            subprocess.run(["shutdown", "-h", "now"])
        else:
            print("Invalid action specified.")
    else:
        print("Unsupported operating system.")


# Example usage:
sleep_or_shutdown("sleep")  # Put the computer to sleep
sleep_or_shutdown("shutdown")  # Initiate a shutdown
