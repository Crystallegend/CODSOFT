import customtkinter as ctk
from math import factorial

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Calculator")
app.geometry("320x400")

label_text = ctk.StringVar()
entry = ctk.CTkEntry(app, textvariable=label_text, corner_radius=8, width=300, state="disabled")
entry.grid(row=0, columnspan=4, padx=10, pady=10)

#________________________________________
#Functions

def evaluate(text):
  error.configure(text="")
  return eval(text)

def add_number(text):
  label_text.set(entry.get()+str(text))

def C_remove():
  label_text.set("")

def square_root():
  if entry.get() != "":
    try:
      label_text.set(str(pow(evaluate(entry.get()), 0.5)))
    except:
      error.configure(text = "Invalid Syntax")
  
def remove():
  label_text.set(entry.get()[0:-1])

def equals():
  if entry.get() != "":
    try:
      label_text.set(str(evaluate(entry.get())))
    except:
      error.configure(text = "Invalid Syntax")

def cfactorial():
  if entry.get() == "":
    return
  try:
    n = evaluate(entry.get())
  except:
    error.configure(text = "Invalid Syntax")
    return
  
  if type(n) != int:
    error.configure(text="Cannot calculate factorial of non-integer numbers")
  elif n > 100:
    error.configure(text="Number is too big to calculate factorial (Range: 0-100)")
  elif n < 0:
    error.configure(text="Cannot calculate factorial for negative numbers")
  else:
    label_text.set(str(factorial(n)))
 
def create_num_button(text):
  button = ctk.CTkButton(app, text=text, width=50, height=50, command=lambda: add_number(text))
  return button

#______________________________________
#Buttons

counter = 1
for row in range(2,5):
  for col in range(3):
    button = create_num_button(counter)
    button.grid(row=row, column=col, padx=5, pady=5)
    counter +=1 

C_button = ctk.CTkButton(app, text="C", width=50, height=50, command=C_remove)
square_root = ctk.CTkButton(app, text="√", width=50, height=50, command=square_root)
division = ctk.CTkButton(app, text="/", width=50, height=50, command=lambda: add_number("/"))
remove = ctk.CTkButton(app, text="<=", width=50, height=50, command=remove)
addition = ctk.CTkButton(app, text="+", width=50, height=50, command=lambda: add_number("+"))
subtraction = ctk.CTkButton(app, text="-", width=50, height=50, command=lambda: add_number("-"))
multiplication = ctk.CTkButton(app, text="x", width=50, height=50, command=lambda: add_number("*"))
equal = ctk.CTkButton(app, text="=", width=50, height=50, command=equals)
factorial_button = ctk.CTkButton(app, text="!", width=50, height=50, command=cfactorial)
zero = create_num_button(0)
dot = ctk.CTkButton(app, text=".", width=50, height=50, command=lambda: add_number("."))
error = ctk.CTkLabel(app, text="", text_color="red")

C_button.grid(row=1, column=0, padx=5, pady=5)
square_root.grid(row=1, column=1, padx=5, pady=5)
division.grid(row=1, column=2, padx=5, pady=5)
remove.grid(row=1, column=3, padx=5, pady=5)
addition.grid(row=2, column=3, padx=5, pady=5)
subtraction.grid(row=3, column=3, padx=5, pady=5)
multiplication.grid(row=4, column=3, padx=5, pady=5)
equal.grid(row=5, column=3, padx=5, pady=5)
factorial_button.grid(row=5, column=0, padx=5, pady=5)
zero.grid(row=5, column=1, padx=5, pady=5)
dot.grid(row=5, column=2, padx=5, pady=5)
error.grid(row=6, columnspan=4, padx=5, pady=5)


app.mainloop()