
import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("تنبيه", "يرجى كتابة مهمة قبل الإضافة.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_tasks()
    else:
        messagebox.showwarning("تنبيه", "يرجى اختيار مهمة للحذف.")

def update_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# نافذة التطبيق
root = tk.Tk()
root.title("Smart Task Manager")

# واجهة المستخدم
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="إضافة مهمة", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="حذف المهمة", command=delete_task)
delete_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

root.mainloop()
