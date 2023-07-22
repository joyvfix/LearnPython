import pyautogui


def screen_monitor(interval, num_screenshots):
    for i in range(num_screenshots):
        # Capture screenshot
        screenshot = pyautogui.screenshot()

        # Save screenshot with a unique name
        screenshot.save(f'screenshot_{i+1}.png')

        # Wait for the specified interval
        pyautogui.sleep(interval)


# Usage example
interval = 10  # Time interval between each screenshot (in seconds)
num_screenshots = 5  # Number of screenshots to capture
screen_monitor(interval, num_screenshots)
