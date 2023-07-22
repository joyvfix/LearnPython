# import pyautogui
# import time


# def laptop_use_reminder():
#     interval = 2 * 60  # 5 minutes in seconds

#     while True:
#         # Display a reminder message box using PyAutoGUI
#         pyautogui.alert('Take a break! Rest your eyes and stretch your body.')

#         # Wait for the specified interval
#         time.sleep(interval)


# # Start the reminder
# laptop_use_reminder()
# (''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''')
import pyautogui
import time
import os


def laptop_use_reminder():
    interval = 1 * 60  # 5 minutes in seconds

    while True:
        # Display a reminder message box using PyAutoGUI
        result = pyautogui.alert(
            'Take a break! Rest your eyes and stretch your body.', button='OK')

        # Check the result of the alert dialog
        if result == 'OK':
            # Continue the loop and wait for the specified interval
            time.sleep(1)
        else:
            # Stop the loop and perform additional actions
            if result == 'Sleep':
                # Put the computer to sleep
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                break
            elif result == 'Activity':
                # Perform some continuous activity (e.g., playing a video)
                # Add your code here for the desired activity
                break
            elif result == 'Shutdown':
                # Shutdown the computer
                os.system("shutdown /s /t 0")
                break


# Start the reminder
laptop_use_reminder()
