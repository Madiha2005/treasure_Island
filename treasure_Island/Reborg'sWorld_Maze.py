import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
import time

def add_instruction():
    instruction = instruction_entry.get()
    time_str = time_entry.get()

    if instruction and time_str:
        try:
            time_format = "%H:%M:%S"
            scheduled_time = datetime.strptime(time_str, time_format)
            current_time = datetime.now()

            if scheduled_time > current_time:
                instructions.append((instruction, scheduled_time))
                instruction_entry.delete(0, tk.END)
                time_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Invalid Time", "Please enter a future time.")
        except ValueError:
            messagebox.showwarning("Invalid Time", "Please enter time in HH:MM:SS format.")
    else:
        messagebox.showwarning("Input Error", "Both instruction and time fields are required.")

def check_reminders():
    current_time = datetime.now()
    for instruction, scheduled_time in instructions:
        if current_time >= scheduled_time:
            messagebox.showinfo("Reminder", instruction)
            instructions.remove((instruction, scheduled_time))

def update_clock_label():
    current_time = datetime.now()
    clock_label.config(text=current_time.strftime("%Y-%m-%d %H:%M:%S"))
    root.after(1000, update_clock_label)

instructions = []

root = tk.Tk()
root.title("Daily Instruction Notepad")

instruction_label = tk.Label(root, text="Instruction:")
instruction_label.pack()

instruction_entry = tk.Entry(root, width=40)
instruction_entry.pack()

time_label = tk.Label(root, text="Time (HH:MM:SS):")
time_label.pack()

time_entry = tk.Entry(root, width=20)
time_entry.pack()

add_button = tk.Button(root, text="Add Instruction", command=add_instruction)
add_button.pack()

clock_label = tk.Label(root, text="", font=("Helvetica", 12))
clock_label.pack()
update_clock_label()

reminder_thread = threading.Thread(target=check_reminders)
reminder_thread.daemon = True
reminder_thread.start()

root.mainloop()


