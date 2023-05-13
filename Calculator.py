import tkinter as tk
from tkinter import ttk
import math

# Function to append the clicked number or operator to the input text
def add_to_input(value):
    input_text1.insert(tk.END, value)

# Function to perform the calculation
def calculate():
    try:
        expression = input_text1.get("1.0", tk.END).strip()
        result = None

        # Handling different operators
        if "+" in expression:
            num1, num2 = expression.split("+")
            result = float(num1) + float(num2)
        elif "-" in expression:
            num1, num2 = expression.split("-")
            result = float(num1) - float(num2)
        elif "*" in expression:
            num1, num2 = expression.split("*")
            result = float(num1) * float(num2)
        elif "/" in expression:
            num1, num2 = expression.split("/")
            result = float(num1) / float(num2)
        elif "%" in expression:
            num1, num2 = expression.split("%")
            result = float(num1) % float(num2)
        elif "^" in expression:
            num1, num2 = expression.split("^")
            result = math.pow(float(num1), float(num2))
        elif "√" in expression:
            num = expression[1:]
            result = math.sqrt(float(num))
        
        if result is not None:
            input_text1.delete("1.0", tk.END)
            input_text1.insert(tk.END, str(result))
        else:
            input_text1.delete("1.0", tk.END)
            input_text1.insert(tk.END, "Invalid input")
    except (ValueError, SyntaxError):
        input_text1.delete("1.0", tk.END)
        input_text1.insert(tk.END, "Invalid input")
        
# Function to calculate CGPA
def calculate_cgpa():
    total_credits = 0
    total_grade_points = 0
    grade_points = {
        "A": 4.0,"A-": 3.7,"B+": 3.3,"B": 3.0,"B-": 2.7,"C+": 2.3,"C": 2.0,"C-": 1.7,"D+": 1.3,"D": 1.0,"F": 0.0
    }
    for entry in grade_entries:
        try:
            grade = entry.get().upper()
            credit = 3.0 
            if grade in grade_points:
                total_credits += credit
                total_grade_points += grade_points[grade] * credit
        except ValueError:
            pass
    if total_credits > 0:
        cgpa = total_grade_points / total_credits
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, f"CGPA: {cgpa:.2f}")
    else:
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, "Invalid input")

def selection_changed(event):
    selected_item = combo.get()
    Subject_label.config(text="Course: " + selected_item)
    create_grade_boxes(int(selected_item))

def create_grade_boxes(num_boxes):
    # Destroy previously created grade entry boxes
    for widget in grade_frame.winfo_children():
        widget.destroy()
    # Create new grade entry boxes
    for i in range(num_boxes):
        label = tk.Label(grade_frame, text=f"Course {i+1} Grade:")
        label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        combo = ttk.Combobox(grade_frame, values=["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"])
        combo.grid(row=i, column=1, padx=10, pady=5)
        grade_entries.append(combo)

        
# Create the main window
window = tk.Tk()
window.title("Calculator And CGPA Calculator")
window.geometry("335x600")
window.config(bg="#bea9de") 
window.resizable(False, True)
# Create input text widget
input_text1 = tk.Text(window, width=900, height=2, font=("Arial", 15), bg="white", fg="black")
input_text1.place(x=0,y=0)


# Create number buttons
button_0 = tk.Button(window, text="0", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("0"))
button_0.place(x=0, y=250)
button_1 = tk.Button(window, text="1", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("1"))
button_1.place(x=0, y=55)
button_2 = tk.Button(window, text="2", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("2"))
button_2.place(x=65, y=55)
button_3 = tk.Button(window, text="3", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("3"))
button_3.place(x=131, y=55)
button_4 = tk.Button(window, text="4", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("4"))
button_4.place(x=0, y=120)
button_5 = tk.Button(window, text="5", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("5"))
button_5.place(x=65, y=120)
button_6 = tk.Button(window, text="6", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("6"))
button_6.place(x=131, y=120)
button_7 = tk.Button(window, text="7", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("7"))
button_7.place(x=0, y=185)
button_8 = tk.Button(window, text="8", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("8"))
button_8.place(x=65, y=185)
button_9 = tk.Button(window, text="9", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("9"))
button_9.place(x=131, y=185)
button_dot = tk.Button(window, text=".", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("."))
button_dot.place(x=65, y=250)

# Create operator buttons
button_plus = tk.Button(window, text="+", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("+"))
button_plus.place(x=200, y=55)
button_minus = tk.Button(window, text="-", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("-"))
button_minus.place(x=200, y=120)
button_mul = tk.Button(window, text="*", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("*"))
button_mul.place(x=200, y=185)
button_div = tk.Button(window, text="/", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("/"))
button_div.place(x=200, y=250)
button_divisor = tk.Button(window, text="%", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("%"))
button_divisor.place(x=265, y=250)
button_Pow = tk.Button(window, text="^", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("^"))
button_Pow.place(x=265, y=185)
button_root= tk.Button(window, text="√", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: add_to_input("√"))
button_root.place(x=265, y=120)

# Create Clear button
button_ac= tk.Button(window, text="AC", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=lambda: input_text1.delete("1.0", tk.END))
button_ac.place(x=265, y=55)

# Create equals button
button_equals = tk.Button(window, text="=", width=5, height=2, font=("Arial", 15), bg="white", fg="black", command=calculate)
button_equals.place(x=131, y=250)

# Create CGPA Counter
text_label = tk.Label(window, text="CGPA Calculator", font=("Arial", 15), bg="white", fg="black")
text_label.place(x=90, y=350)

# Create input text 
input_text = tk.Text(window, width=900, height=2, font=("Arial", 15), bg="white", fg="black")
input_text.place(x=0,y=400)

# Create a label for the Course item
Subject_label = tk.Label(window, text="Course", font=("Arial", 15), bg="white", fg="black")
Subject_label.place(x=0,y=480)
# Create a course Combobox
combo = ttk.Combobox(window, width=10, font=("Arial", 15),values=[str(i) for i in range(1, 14)])
combo.current(0)
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=0,y=520)

grade_frame = tk.Frame(window)
grade_frame.place(x=40,y=555)
grade_entries = []

button_calculate_cgpa = tk.Button(window, text="Calculate CGPA", width=13, height=2, font=("Arial", 15), bg="white", fg="black", command=calculate_cgpa)
button_calculate_cgpa.place(x=160, y=470)
# Start the main loop
window.mainloop()