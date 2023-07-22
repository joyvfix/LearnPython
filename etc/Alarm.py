import pyautogui
import time
import winsound


def set_alarm(message, duration):
    # Wait for the specified duration
    time.sleep(duration)

    # Display a message box using PyAutoGUI
    pyautogui.alert(message)

    # Play a sound using winsound
    frequency = 1000  # Set the frequency (1000Hz in this example)
    # Set the duration in milliseconds (2 seconds in this example)
    duration = 2000
    winsound.Beep(frequency, duration)


# Set the alarm with a message and duration
message = "Wake up! It's time!"
duration = 5  # Set the duration in seconds
set_alarm(message, duration)
