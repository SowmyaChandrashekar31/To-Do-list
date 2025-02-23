import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = tasks_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Info", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks_listbox.delete(0, tk.END)
            for task in file:
                tasks_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")
root.geometry("700x700")
root.configure(bg="#1D0C4E")

task_entry = tk.Entry(root, bg="#D6CECA",width=50)
task_entry.pack(pady=15)

add_button = tk.Button(root, text="Add Task",bg="green",width=20,command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task",bg="#de0e21",width=20, command=remove_task)
remove_button.pack()

save_button = tk.Button(root, text="Save Tasks", bg="#b4d6f4",width=20,command=save_tasks)
save_button.pack()

load_button = tk.Button(root, text="Load Tasks",bg="#fae951",width=20, command=load_tasks)
load_button.pack()

tasks_listbox = tk.Listbox(root, width=50,bg="#d4dbda", height=15)
tasks_listbox.pack(pady=10)

load_tasks()
root.mainloop()
