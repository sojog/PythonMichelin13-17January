
import tkinter as tk

window = tk.Tk()
print(window)

width =  400
height = 600
x = 100
y = 150

window.geometry(f"{width}x{height}+{x}+{y}")

window.mainloop()
