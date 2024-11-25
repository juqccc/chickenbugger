import tkinter as tk
from tkinter import messagebox
import threading
import time

def countdown():
    for i in range(10, 0, -1):
        label.config(text=str(i))
        time.sleep(1)

def start_countdown():
    thread = threading.Thread(target=countdown)
    thread.start()

# Create the Tkinter window
root = tk.Tk()
root.title("Countdown GUI")
root.geometry("200x200")

# Create a label to display the countdown
label = tk.Label(root, text="", font=("Helvetica", 48))
label.pack(pady=20)

# Create a button to start the countdown
start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack()

# Make the window movable
root.overrideredirect(True)  # Remove window decorations
root.attributes("-topmost", True)  # Keep window on top
root.mainloop()
