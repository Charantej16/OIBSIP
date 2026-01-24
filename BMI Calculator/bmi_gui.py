import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "bmi_data.csv"

# Save data to CSV
def save_data(name, weight, height, bmi, category):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, weight, height, bmi, category, datetime.now()])

# Calculate BMI
def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if name == "":
            messagebox.showerror("Error", "Name is required")
            return

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter valid weight and height")
            return

        bmi = round(weight / (height * height), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi} ({category})")

        save_data(name, weight, height, bmi, category)

    except ValueError:
        messagebox.showerror("Error", "Please enter numeric values")

# Show BMI history graph
def show_graph():
    bmis = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                bmis.append(float(row[3]))

        if not bmis:
            messagebox.showinfo("Info", "No data to show")
            return

        plt.plot(bmis)
        plt.title("BMI Trend")
        plt.xlabel("Entries")
        plt.ylabel("BMI")
        plt.show()

    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found")

# GUI Window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x350")

tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Weight (kg)").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Height (m)").pack()
height_entry = tk.Entry(window)
height_entry.pack()

tk.Button(window, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
tk.Button(window, text="Show BMI Graph", command=show_graph).pack()

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
