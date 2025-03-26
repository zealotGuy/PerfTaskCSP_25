import tkinter as tk
from tkinter import messagebox

def gradient(canvas, width, height):
    canvas.create_rectangle(0, 0, width, height, fill="#ADD8E6", outline="#ADD8E6")
    canvas.create_rectangle(0, 0, width, height, fill="#40E0D0", outline="#40E0D0", stipple="gray12")

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def complete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        task = f"{task} - Completed"
        tasks_listbox.insert(tk.END, task)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

def complete_all_tasks():
    for i in range(tasks_listbox.size()):
        task = tasks_listbox.get(i)
        tasks_listbox.delete(i)
        tasks_listbox.insert(tk.END, f"{task} - Completed")

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x500")

canvas = tk.Canvas(root, width=400, height=500)
canvas.pack(fill="both", expand=True)

gradient(canvas, 400, 500)

task_entry = tk.Entry(root, width=30)
task_entry.place(x=50, y=40)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.place(x=50, y=70)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.place(x=50, y=100)

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.place(x=50, y=130)

complete_all_button = tk.Button(root, text="Complete All Tasks", command=complete_all_tasks)
complete_all_button.place(x=50, y=160)

tasks_listbox = tk.Listbox(root, width=40, height=10)
tasks_listbox.place(x=50, y=200)

root.mainloop()
