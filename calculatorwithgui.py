import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from ttkbootstrap import Style

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"

    label_result.config(text="Result: " + str(result))

# Create a Tkinter window
window = tk.Tk()
window.title("Calculator")

# Apply ttkbootstrap style
style = Style(theme='minty')

# Create input fields for numbers
label_num1 = ttk.Label(window, text="Number 1:")
label_num1.pack(pady=10)
entry_num1 = ttk.Entry(window)
entry_num1.pack(pady=5)

label_num2 = ttk.Label(window, text="Number 2:")
label_num2.pack(pady=10)
entry_num2 = ttk.Entry(window)
entry_num2.pack(pady=5)

# Create radio buttons for operations
operation_var = tk.StringVar()
operation_var.set("Addition")

label_operation = ttk.Label(window, text="Operation:")
label_operation.pack(pady=10)

radio_addition = ttk.Radiobutton(window, text="Addition", variable=operation_var, value="Addition")
radio_addition.pack(anchor='w', pady=5)

radio_subtraction = ttk.Radiobutton(window, text="Subtraction", variable=operation_var, value="Subtraction")
radio_subtraction.pack(anchor='w', pady=5)

radio_multiplication = ttk.Radiobutton(window, text="Multiplication", variable=operation_var, value="Multiplication")
radio_multiplication.pack(anchor='w', pady=5)

radio_division = ttk.Radiobutton(window, text="Division", variable=operation_var, value="Division")
radio_division.pack(anchor='w', pady=5)

# Create a button to calculate the result
button_calculate = ttk.Button(window, text="Calculate", command=calculate, style='AccentButton')
button_calculate.pack(pady=10)

# Create a label to display the result
label_result = ttk.Label(window, text="Result:")
label_result.pack(pady=10)

# Apply ttkthemes style
ttk.Style().theme_use('clam')

# Start the Tkinter event loop
window.mainloop()
