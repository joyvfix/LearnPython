import time
from plyer import notification
import datetime


def set_daily_reminder(title, message, hour, minute):
    now = datetime.datetime.now()
    reminder_time = datetime.datetime(
        now.year, now.month, now.day, hour, minute)
    time_difference = reminder_time - now

    # If the reminder time has already passed for today, set it for tomorrow
    if time_difference.total_seconds() < 0:
        reminder_time += datetime.timedelta(days=1)

    time_difference = reminder_time - now
    seconds_to_reminder = time_difference.total_seconds()

    # Wait until the reminder time is reached
    time.sleep(seconds_to_reminder)

    # Display the notification
    notification.notify(title=title, message=message, timeout=10)


# Example usage: Set a reminder at 8:00 AM
set_daily_reminder(
    "Daily Reminder", "Don't forget to complete your tasks!", 8, 0)
