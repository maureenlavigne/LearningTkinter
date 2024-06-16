# https://dev.to/phylis/introducing-kids-to-coding-through-tkinter-a-fun-path-to-pythons-graphical-user-interfaces-135c
# https://www.studytonight.com/tkinter/python-tkinter-widgets
# https://www.w3resource.com/python-exercises/tkinter/python-tkinter-events-and-event-handling-exercise-3.php
# short for "Tk Interface
# python's standard library for creating graphical user interfaces
# beginner-friendly but also robust enough to handle more advanced projects
# can run on Windows, macOS, and Linux, versatile choice for young coders using various operating systems

# Idea 1 : craft a simple calculator

# Import the tkinter module for GUI
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Pink Calculator")

# Create an input field
entry = tk.Entry(root, highlightcolor="black", highlightthickness=5,
                 width=20, bg="pink", font=("Times", 20, "bold"))
entry.grid(row=0, column=0, columnspan=5)

# Create buttons for digits (0-9)
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", ".", "=", "/"
]
row, col = 1, 0

for button in buttons:
    tk.Button(root, text=button, bg="pink", padx=20, pady=20, font=("Times", 16, "bold"),
              command=lambda button=button: button_click(button)).grid(row=row, column=col, columnspan=1, sticky="ew")
    col += 1
    if col > 3:
        col = 0
        row += 1
# Create a Backspace button
tk.Button(root, text="←", padx=20, pady=20, bg="pink", font=("Times", 16, "bold"),
          command=lambda: button_click("←")).grid(row=5, column=3, columnspan=1)

# Create a Clear (C) button
tk.Button(root, text="C", width=15, padx=20, pady=20, bg="pink", font=("Times", 16, "bold"),
          command=lambda: button_click("C")).grid(row=5, column=0, columnspan=3)


# Function to update the input field
def button_click(value):
    current = entry.get()
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif value == "←":
        entry.delete(len(current) - 1, tk.END)
    else:
        entry.insert(tk.END, value)



# Start the Tkinter main loop
root.mainloop()