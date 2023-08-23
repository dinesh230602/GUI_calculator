import tkinter as tk

def evaluate_expression():
    try:
        result = eval(entry.get())
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text="Error: Invalid Expression")

def clear_entry():
    entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("CALCULATOR")

# Create the input entry widget
entry = tk.Entry(root, width=30, font=('Helvetica', 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for button_text, row, col in buttons:
    button = tk.Button(root, text=button_text, width=10, height=3, font=('Helvetica', 18),
                       command=lambda text=button_text: entry.insert(tk.END, text) if text != '=' else evaluate_expression())
    button.grid(row=row, column=col, padx=5, pady=5)

# Create the result label
result_label = tk.Label(root, text="Result: ", font=('Helvetica', 18))
result_label.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Create the clear button
clear_button = tk.Button(root, text="Clear", width=10, height=3, font=('Helvetica', 18), command=clear_entry)
clear_button.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

# Start the main event loop
root.mainloop()