import tkinter as tk
import time

root = tk.Tk()
root.title("Clock")

def time_update():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, time_update)

label = tk.Label(root, font=("times", 20, "bold"))
label.pack()

time_update()

root.mainloop()

