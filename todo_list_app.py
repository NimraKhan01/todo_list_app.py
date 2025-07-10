import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple To-Do list")

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Input Error","Task cannot be empty!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        tasks.pop(selected_task)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please Select a task to delete.")


entry = tk.Entry(root, width = 40)
entry.pack(pady= 10)

add_btn = tk.Button(root, text = "Add Task", width = 20, command = add_task)
add_btn.pack()

del_btn = tk.Button(root, text = "Delete Task", width = 20, command = delete_task)
del_btn.pack()

listbox = tk.Listbox(root,width = 50, height = 10)
listbox.pack(pady = 10)
root.mainloop()



