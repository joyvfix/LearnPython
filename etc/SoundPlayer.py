# # import libraries
# from winsound import PlaySound
# from pyautogui import PAUSE
# from pygame import mixer
# from tkinter import *
# import tkinter.font as font
# from tkinter import filedialog

# # creating the root window
# root = Tk()
# root.title('DataFlair python MP3 Music player app')

# # initialize mixer
# mixer.init()

# # create the listbox to contain songs
# songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=(
#     'arial', 15), height=12, width=47, selectbackground="gray", selectforeground="black")
# songs_list.grid(columnspan=9)

# # font is defined which is to be used for the button font
# defined_font = font.Font(family="helvetica")

# # play button
# play_button = Button(root, text="play", width=7, command=PlaySound)
# play_button['font'] = defined_font
# play_button.grid(row=1, column=0)

# # pause button
# pause_button = Button(root, text="pause", width=7, command=PAUSE)
# pause_button['font'] = defined_font
# pause_button.grid(row=1, column=1)

# mainloop()
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# # import libraries
# from winsound import PlaySound, SND_FILENAME, SND_ASYNC
# from pyautogui import PAUSE
# from tkinter import *
# from tkinter import filedialog
# import tkinter.font as font

# # creating the root window
# root = Tk()
# root.title('DataFlair python MP3 Music player app')

# # initialize mixer
# try:
#     mixer.init()
# except:
#     pass

# # create the listbox to contain songs
# songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=(
#     'arial', 15), height=12, width=47, selectbackground="gray", selectforeground="black")
# songs_list.grid(columnspan=9)

# # font is defined which is to be used for the button font
# defined_font = font.Font(family="helvetica")


# def play_music():
#     try:
#         selected_song = songs_list.get(songs_list.curselection())
#         PlaySound(selected_song, SND_FILENAME | SND_ASYNC)
#     except:
#         pass


# def pause_music():
#     PAUSE


# # play button
# play_button = Button(root, text="play", width=7, command=play_music)
# play_button['font'] = defined_font
# play_button.grid(row=1, column=0)

# # pause button
# pause_button = Button(root, text="pause", width=7, command=pause_music)
# pause_button['font'] = defined_font
# pause_button.grid(row=1, column=1)

# mainloop()
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize pygame
pygame.init()

# Function to select a music file using tkinter's file dialog


def choose_music_file():
    file_path = filedialog.askopenfilename()
    return file_path

# Function to play the selected music file


def play_music():
    file_path = choose_music_file()
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

# Function to pause the music


def pause_music():
    pygame.mixer.music.pause()

# Function to resume the music


def unpause_music():
    pygame.mixer.music.unpause()

# Function to stop the music


def stop_music():
    pygame.mixer.music.stop()


# Create the Tkinter window
root = tk.Tk()
root.title('Simple Music Player')

# Play button
play_button = tk.Button(root, text='Play', command=play_music)
play_button.pack(pady=10)

# Pause button
pause_button = tk.Button(root, text='Pause', command=pause_music)
pause_button.pack(pady=5)

# Unpause (Resume) button
unpause_button = tk.Button(root, text='Unpause', command=unpause_music)
unpause_button.pack(pady=5)

# Stop button
stop_button = tk.Button(root, text='Stop', command=stop_music)
stop_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
