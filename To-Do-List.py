import customtkinter as ctk
import tkinter as tk

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("To-Do List App")
app.geometry("700x500")

top_bar = ctk.CTkLabel(app, text="TO-DO List", height=30, font=("Arial", 18))
top_bar.pack(fill=ctk.X, padx=10, pady=20)

def add_task():
  task_text = entry.get()
  entry.delete(0, tk.END)
  listbox.insert(tk.END, task_text)

def delete_task():
  selected_index = listbox.curselection()
  if selected_index:
    listbox.delete(selected_index[0])

def edit_task():
  selected_index = listbox.curselection()
  if selected_index:
    task_text = listbox.get(selected_index[0])

    edit_window = tk.Tk()
    edit_window.title("Edit Task")

    edit_label = tk.Label(edit_window, text="Edit Task:")
    edit_label.pack()

    edit_entry = tk.Entry(edit_window, width=50)
    edit_entry.insert(0, task_text)
    edit_entry.pack()

    def save_task():
      edited_text = edit_entry.get()
      listbox.delete(selected_index[0])
      listbox.insert(selected_index[0], edited_text)
      edit_window.destroy() 

    save_button = tk.Button(edit_window, text="Save", command=save_task)
    save_button.pack()

    edit_window.mainloop()

Add_frame = ctk.CTkFrame(app)
label1 = ctk.CTkLabel(Add_frame, text="Add Items",  font=("Arial", 14))
entry = ctk.CTkEntry(Add_frame, placeholder_text="Enter Task Name", corner_radius=10, width=250)
button = ctk.CTkButton(Add_frame, text="Add", font=("Arial", 14), command=add_task)
Add_frame.pack(fill=ctk.X, pady=10)
label1.pack()
entry.pack()
button.pack()

label2 = ctk.CTkLabel(app, text="Tasks", font=("Arial", 18))
listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=50, font=("Arial", 12), bd=0, bg="grey", selectbackground="black", yscrollcommand=True)
label2.pack(pady=15)
listbox.pack()

button_frame = ctk.CTkFrame(app)
edit_button = ctk.CTkButton(button_frame, text="Edit", command=edit_task)
delete_button = ctk.CTkButton(button_frame, text="Delete", command=delete_task, fg_color="red")
button_frame.pack(pady=10)
edit_button.pack(side=ctk.LEFT, padx=2)
delete_button.pack(side=ctk.RIGHT, padx=2)

app.mainloop()