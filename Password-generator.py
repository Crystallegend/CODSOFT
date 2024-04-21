import customtkinter as ctk
import string
import random

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Password Generator")
app.geometry("300x400")

def generate_password():
    try:  
      length = int(entry_length.get())
      complexity = int(entry_complexity.get())
    

      if length < 1 or length > 16:
        msg.configure(text="Invalid Length", text_color="red")
        return
      if complexity < 1 or complexity > 4:
        msg.configure(text="Invalid Complexity", text_color="red")
        return
    except:
      msg.configure(text="Please enter integer value", text_color="red")
      return 
    
    char_sets = {
      1: string.ascii_lowercase,
      2: string.ascii_lowercase + string.ascii_uppercase,
      3: string.ascii_lowercase + string.ascii_uppercase + string.digits,
      4: string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation,
    }

    char_set = char_sets[complexity]
    res = ''.join(random.SystemRandom().choice(char_set) for i in range(length))
    password.set(res)
    msg.configure(text="Password Generated", text_color="green")

def copy_text():
  app.clipboard_append(entry_pass.get())
  msg.configure(text="Password Copied", text_color="green")

def reset():
  entry_complexity.delete(0, ctk.END)
  entry_length.delete(0, ctk.END)
  password.set("")
  msg.configure(text="")

label = ctk.CTkLabel(app, text="Password Generator", font=("Arial", 20))
label.grid(row=0, columnspan=5, padx=20, pady=10)

label_complexity = ctk.CTkLabel(app, text="Enter complexity:")
entry_complexity = ctk.CTkEntry(app, placeholder_text="1-4")
label_complexity.grid(row=1, columnspan=2, padx=5, pady=5)
entry_complexity.grid(row=1, column=2, columnspan=3, padx=5, pady=5)

label_length = ctk.CTkLabel(app, text="Enter password length:")
entry_length = ctk.CTkEntry(app, placeholder_text="1-16")
label_length.grid(row=2, columnspan=2, padx=5, pady=5)
entry_length.grid(row=2, column=2, columnspan=3, padx=5, pady=5)

msg = ctk.CTkLabel(app, text="", text_color="red")
msg.grid(row=3, column=1, columnspan=3, padx=3, pady=3)

label_pass = ctk.CTkLabel(app, text="Generated Password", font=("Arial", 16))
password = ctk.StringVar()
entry_pass = ctk.CTkEntry(app, state="disabled", textvariable=password, text_color="green", font=("Arial", 14)) 
label_pass.grid(row=4, column=1, columnspan=3, padx=10, pady=10)
entry_pass.grid(row=5, column=1, columnspan=3, padx=10, pady=5)

generate = ctk.CTkButton(app, text="Generate", command=generate_password)
copy_text = ctk.CTkButton(app, text="Copy", command=copy_text, fg_color="green")
reset = ctk.CTkButton(app, text="Reset", command=reset, fg_color="red")
generate.grid(row=6, column=1, columnspan=3, padx=5, pady=10)
copy_text.grid(row=7, column=1, columnspan=3, padx=5, pady=5)
reset.grid(row=8, column=1, columnspan=3, padx=5, pady=5)

app.mainloop()