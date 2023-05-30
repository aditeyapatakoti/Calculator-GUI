import tkinter as tk

def button_click(number):
    current = input_display.get()
    input_display.delete(0, tk.END)
    input_display.insert(tk.END, current + str(number))

def button_clear():
    input_display.delete(0, tk.END)
    output_display.config(text="")

def calculate():
    expression = input_display.get()
    try:
        result = eval(expression)
        output_display.config(text=str(result))
    except:
        output_display.config(text="Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")  # Set window size

# Create the input display widget
input_display = tk.Entry(window, width=20, font=('Arial', 20))
input_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the output display label
output_display = tk.Label(window, width=20, font=('Arial', 20), relief=tk.SOLID)
output_display.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")  # Position at the bottom
output_display.grid_columnconfigure(0, weight=1)  # Expand to fit the width

# Create the number buttons
button_1 = tk.Button(window, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=20, command=lambda: button_click(0))

# Create the operator buttons
button_add = tk.Button(window, text="+", padx=20, pady=20, command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=20, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=20, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=20, pady=20, command=lambda: button_click("/"))
button_equal = tk.Button(window, text="=", padx=20, pady=20, command=calculate)
button_clear = tk.Button(window, text="C", padx=20, pady=20, command=button_clear)

# Bind Enter key to calculate
window.bind("<Return>", lambda event: calculate())

# Position the buttons on the grid
button_1.grid(row=2, column=0, padx=10, pady=10)
button_2.grid(row=2, column=1, padx=10, pady=10)
button_3.grid(row=2, column=2, padx=10, pady=10)
button_4.grid(row=3, column=0, padx=10, pady=10)
button_5.grid(row=3, column=1, padx=10, pady=10)
button_6.grid(row=3, column=2, padx=10, pady=10)
button_7.grid(row=4, column=0, padx=10, pady=10)
button_8.grid(row=4, column=1, padx=10, pady=10)
button_9.grid(row=4, column=2, padx=10, pady=10)
button_0.grid(row=5, column=0, padx=10, pady=10)

button_add.grid(row=2, column=3, padx=10, pady=10)
button_subtract.grid(row=3, column=3, padx=10, pady=10)
button_multiply.grid(row=4, column=3, padx=10, pady=10)
button_divide.grid(row=5, column=3, padx=10, pady=10)
button_equal.grid(row=5, column=2, padx=10, pady=10)
button_clear.grid(row=5, column=1, padx=10, pady=10)

# Adjust column weights
for i in range(4):
    window.columnconfigure(i, weight=1)

# Adjust row weight for output_display
window.rowconfigure(1, weight=1)

# Start the main event loop
window.mainloop()
