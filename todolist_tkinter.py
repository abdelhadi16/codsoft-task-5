import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_task_listbox()
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Task Added", f"Task '{task}' added.")
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for index, task in enumerate(tasks):
        task_listbox.insert(tk.END, f"Task #{index}: {task}")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = tasks.pop(selected_task_index)
        update_task_listbox()
        messagebox.showinfo("Task Deleted", f"Task '{task}' deleted.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

app = tk.Tk()
app.title("To-Do List App")

frame = tk.Frame(app)
frame.pack(pady=50)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=10)

add_task_button = tk.Button(frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(app, width=50, height=10)
task_listbox.pack(pady=10)

delete_task_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_task_button.pack()

app.mainloop()
