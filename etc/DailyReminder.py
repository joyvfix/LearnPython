
import schedule
import time
import tkinter as tk
from tkinter import messagebox


def reminder():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Daily Reminder", "It's time for your daily reminder!")


# Schedule the reminder to occur at a specific time every day
schedule.every().day.at("19:04").do(reminder)

while True:
    schedule.run_pending()
    time.sleep(1)
