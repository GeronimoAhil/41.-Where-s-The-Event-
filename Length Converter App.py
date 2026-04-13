import tkinter as tk
from tkinter import ttk, messagebox

# --- Define conversion factors (base: meters) ---
LENGTH_UNITS = {"Meters": 1.0, "Kilometers": 1000.0, "Miles": 1609.34, "Centimeters": 0.01}

# --- Conversion Logic ---
def convert_length():
    try:
        value = float(entry_value.get())
        factor_from = LENGTH_UNITS[combo_from.get()]
        factor_to = LENGTH_UNITS[combo_to.get()]
        result = value * factor_from / factor_to
        result_var.set(f"Result: {result:.6g} {combo_to.get()}") #
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

# --- GUI Setup ---
root = tk()
root.title("Length Converter")
root.geometry("300x200")

# Widgets
entry_value = ttk.Entry(root)
entry_value.pack(pady=5)
combo_from = ttk.Combobox(root, values=list(LENGTH_UNITS.keys())) #
combo_from.current(0)
combo_from.pack()
combo_to = ttk.Combobox(root, values=list(LENGTH_UNITS.keys()))
combo_to.current(1)
combo_to.pack()
ttk.Button(root, text="Convert", command=convert_length).pack(pady=10)
result_var = tk.StringVar()
ttk.Label(root, textvariable=result_var).pack()

root.mainloop()
