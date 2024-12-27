import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
from my_file import *

def employee_manager(tree_p,root_p,filter_frame_p):
    data_file = 'data/Employees.csv'

    def check_and_add():
        e_id = entry_id.get()
        e_lname = entry_lname.get()
        e_fname = entry_fname.get()
        e_sex = entry_sex.get()
        if not all([e_id, e_lname, e_fname, e_sex]):
            messagebox.showwarning("Помилка", "Будь ласка, заповніть усі поля.")
            return

        new_employee = [e_id, e_lname, e_fname, e_sex]
        with open(data_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row == new_employee:
                    messagebox.showinfo("Результат", "Такий запис вже існує.")
                    return
                elif row[0] == new_employee[0]:
                    messagebox.showinfo("Результат", "Такий айді вже існує.")
                    return

        with open(data_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(new_employee)

        messagebox.showinfo("Результат", "Запис успішно додано.")
        load_employees(tree_p,root_p,filter_frame_p)
        entry_id.delete(0, tk.END)
        entry_lname.delete(0, tk.END)
        entry_fname.delete(0, tk.END)
        entry_sex.set('') 

    root = tk.Tk()
    root.title("Додавання працівників")

    frame = tk.Frame(root)
    frame.pack(pady=10, padx=10)

    fields = [
        ("ID:", "entry_id"),
        ("Прізвище:", "entry_lname"),
        ("Ім'я:", "entry_fname"),
        ("Стать:", "entry_sex")
    ]

    entries = {}
    for i, (label_text, var_name) in enumerate(fields):
        label = tk.Label(frame, text=label_text)
        label.grid(row=i, column=0, sticky="w")

        if var_name == "entry_sex":
            entry = ttk.Combobox(frame, values=["чоловік", "жінка"], state="readonly")
        else:
            entry = tk.Entry(frame)

        entry.grid(row=i, column=1)
        entries[var_name] = entry

    entry_id = entries["entry_id"]
    entry_lname = entries["entry_lname"]
    entry_fname = entries["entry_fname"]
    entry_sex = entries["entry_sex"]

    btn_submit = tk.Button(root, text="Перевірити та додати", command=check_and_add)
    btn_submit.pack(pady=5)

    root.mainloop()
