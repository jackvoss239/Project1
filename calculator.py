import tkinter as tk
import math
def on_number_click(number):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(number))

def on_clear_click():
    entry.delete(0, tk.END)
    global current_result
    current_result = 0
    global operation
    operation = None

def on_operator_click(operator):
    global current_result
    global operation
    if not entry.get():
        return
    if operation:
        on_equals_click()
    current_result = float(entry.get())
    operation = operator
    entry.delete(0, tk.END)

def on_equals_click():
    global current_result
    global operation
    if not operation or not entry.get():
        return
    second_number = float(entry.get())
    try:
        if operation == '+':
            current_result += second_number
        elif operation == '-':
            current_result -= second_number
        elif operation == '*':
            current_result *= second_number
        elif operation == '/':
            current_result /= second_number
        elif operation == 'exp':
            current_result = base_number ** second_number
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Cannot Divide by 0")
        operation = None
        return

    entry.delete(0, tk.END)
    entry.insert(0, current_result)
    operation = None

def on_sin_click():
    if not entry.get():
        return
    number = float(entry.get())
    result = math.sin(math.radians(number))
    entry.delete(0, tk.END)
    entry.insert(0, result)

def on_cos_click():
    if not entry.get():
        return
    number = float(entry.get())
    result = math.cos(math.radians(number))
    entry.delete(0, tk.END)
    entry.insert(0, result)

def on_tan_click():
    if not entry.get():
        return
    number = float(entry.get())
    result = math.tan(math.radians(number))
    entry.delete(0, tk.END)
    entry.insert(0, result)

def on_factorial_click():
    if not entry.get():
        return
    number = int(entry.get())
    result = math.factorial(number)
    entry.delete(0, tk.END)
    entry.insert(0, result)

def on_exponent_click():
    global base_number
    global operation
    if not entry.get():
        return
    base_number = float(entry.get())
    operation = 'exp'
    entry.delete(0, tk.END)

def on_log_click():
    if not entry.get():
        return
    number = float(entry.get())
    if number <= 0:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")
        return
    result = math.log10(number)
    entry.delete(0, tk.END)
    entry.insert(0, result)

def on_ln_click():
    if not entry.get():
        return
    number = float(entry.get())
    if number <= 0:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")
        return
    result = math.log(number)
    entry.delete(0, tk.END)
    entry.insert(0, result)

def on_sqrt_click():
    if not entry.get():
        return
    number = float(entry.get())
    if number < 0:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")
        return
    result = math.sqrt(number)
    entry.delete(0, tk.END)
    entry.insert(0, result)

def on_decimal_point_click():
    current_text = entry.get()
    if "." not in current_text:
        entry.insert(tk.END, ".")

def on_pi_click():
    entry.delete(0, tk.END)
    entry.insert(0, math.pi)


root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, width=15, font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=4)


number_buttons = [
    tk.Button(root, text=str(number), command=lambda number=number: on_number_click(number), font=("Arial", 18), width=5, height=2)
    for number in range(1, 10)
]

for index, button in enumerate(number_buttons):
    button.grid(row=(3 - index // 3), column=(index % 3))

zero_button = tk.Button(root, text="0", command=lambda: on_number_click(0), font=("Arial", 18), width=5, height=2)
zero_button.grid(row=4, column=1)


add_button = tk.Button(root, text="+", command=lambda: on_operator_click('+'), font=("Arial", 18), width=5, height=2)
add_button.grid(row=3, column=3)
subtract_button = tk.Button(root, text="-", command=lambda: on_operator_click('-'), font=("Arial", 18), width=5, height=2)
subtract_button.grid(row=2, column=3)
multiply_button = tk.Button(root, text="*", command=lambda: on_operator_click('*'), font=("Arial", 18), width=5, height=2)
multiply_button.grid(row=1, column=3)
divide_button = tk.Button(root, text="/", command=lambda: on_operator_click('/'), font=("Arial", 18), width=5, height=2)
divide_button.grid(row=4, column=3)
sin_button = tk.Button(root, text="sin", command=on_sin_click, font=("Arial", 18), width=5, height=2)
sin_button.grid(row=5, column=0)
cos_button = tk.Button(root, text="cos", command=on_cos_click, font=("Arial", 18), width=5, height=2)
cos_button.grid(row=5, column=1)
tan_button = tk.Button(root, text="tan", command=on_tan_click, font=("Arial", 18), width=5, height=2)
tan_button.grid(row=5, column=2)
factorial_button = tk.Button(root, text="!", command=on_factorial_click, font=("Arial", 18), width=5, height=2)
factorial_button.grid(row=5, column=3)
exponent_button = tk.Button(root, text="^", command=on_exponent_click, font=("Arial", 18), width=5, height=2)
exponent_button.grid(row=6, column=0)
log_button = tk.Button(root, text="log", command=on_log_click, font=("Arial", 18), width=5, height=2)
log_button.grid(row=6, column=1)
ln_button = tk.Button(root, text="ln", command=on_ln_click, font=("Arial", 18), width=5, height=2)
ln_button.grid(row=6, column=2)
sqrt_button = tk.Button(root, text="√", command=on_sqrt_click, font=("Arial", 18), width=5, height=2)
sqrt_button.grid(row=6, column=3)
decimal_point_button = tk.Button(root, text=".", command=on_decimal_point_click, font=("Arial", 18), width=5, height=2)
decimal_point_button.grid(row=7, column=0)
pi_button = tk.Button(root, text="π", command=on_pi_click, font=("Arial", 18), width=5, height=2)
pi_button.grid(row=7, column=1)


clear_button = tk.Button(root, text="C", command=on_clear_click, font=("Arial", 18), width=5, height=2)
clear_button.grid(row=4, column=0)
equals_button = tk.Button(root, text="=", command=on_equals_click, font=("Arial", 18), width=5, height=2)
equals_button.grid(row=4, column=2)

current_result = 0
operation = None

root.resizable(False, False)

root.mainloop()
