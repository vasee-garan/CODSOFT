import tkinter as tk

tasks = []

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry_task.delete(0, tk.END)
        lbl_status.config(text="Task added successfully.")
    else:
        lbl_status.config(text="Task cannot be empty.")

def view_task():
    if len(tasks) == 0:
        lbl_status.config(text="No tasks.")
    else:
        task_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
        lbl_status.config(text=task_list)

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        del tasks[index]
        update_listbox()
        lbl_status.config(text="Task deleted.")
    except IndexError:
        lbl_status.config(text="Please select a task to delete.")

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        listbox_tasks.insert(tk.END, f"{i}. {task}")

def perform_action():
    choice = var.get()
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        delete_task()

root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

action_choices = [("Add Task", 1), ("View Tasks", 2), ("Delete Task", 3)]
var = tk.IntVar()
var.set(1)  # Default choice is to add task

for text, choice in action_choices:
    tk.Radiobutton(root, text=text, variable=var, value=choice).pack()

button_perform_action = tk.Button(root, text="Perform Action", width=48, command=perform_action)
button_perform_action.pack()

lbl_status = tk.Label(root, text="", fg="blue")
lbl_status.pack()

root.mainloop()
