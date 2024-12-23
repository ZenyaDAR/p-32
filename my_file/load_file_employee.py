from my_file.file_show import load_file_csv
from tkinter import *
from tkinter import ttk
from treeview import *

def filter_treeview(columns, rows, tree, combos, gender_vars):
    selected_lastname = combos[0].get()
    selected_firstname = combos[1].get()
    selected_gender = []
    
    for var, gender in zip(gender_vars, ["чоловік", "жінка"]):
        if var.get() == 1:
            selected_gender.append(gender)

    for item in tree.get_children():
        tree.delete(item)

    tree['columns'] = columns
    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, anchor='center')

    for row in rows[1:]:
        if (
            (selected_lastname == "Усі" or row[1] == selected_lastname) and
            (selected_firstname == "Усі" or row[2] == selected_firstname) and
            (len(selected_gender) == 0 or row[3] in selected_gender)
        ):
            tree.insert("", 'end', values=row)

    tree.grid()

def load_employees(window, root, frame_main, frame_secondary):
    clear_frame(frame_main)
    clear_frame(frame_secondary)
    frame_secondary.grid_remove()
    frame_main.grid()

    csv_file = "data/Employees.csv"
    employee_rows = load_file_csv(csv_file)
    lastnames = list_combo(employee_rows, 1)
    firstnames = list_combo(employee_rows, 2)

    columns = ['ID', 'Прізвище', 'Ім\'я та по батькові', 'Стать']
    show_tree(columns, employee_rows, window)
    adjust_window_size(root, window)
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # Filter for Last Name
    label1 = Label(frame_main, text='Прізвище', background='#168b8d')
    label1.grid(row=0, column=0, sticky='nw', padx=1, pady=1)
    combo1 = ttk.Combobox(frame_main, values=["Усі"] + lastnames, state='readonly')
    combo1.set('Усі')
    combo1.grid(row=0, column=1, sticky='nw', padx=1, pady=1)

    # Filter for First Name
    label2 = Label(frame_main, text='Ім\'я', background='#168b8d')
    label2.grid(row=1, column=0, sticky='nw', padx=1, pady=1)
    combo2 = ttk.Combobox(frame_main, values=["Усі"] + firstnames, state='readonly')
    combo2.set('Усі')
    combo2.grid(row=1, column=1, sticky='nw', padx=1, pady=1)

    combos = (combo1, combo2)

    # Filter for Gender
    label3 = Label(frame_main, text='Стать', background='#168b8d')
    label3.grid(row=0, column=2, sticky='nw', padx=1, pady=1)

    cframe = Frame(frame_main, bg='#168b8d')
    cframe.grid(row=0, column=3, rowspan=5, sticky='nsew', padx=1, pady=1)

    genders = ["чоловік", "жінка"]
    gender_vars = [IntVar() for _ in genders]

    for i, gender in enumerate(genders):
        check = Checkbutton(cframe, text=gender, variable=gender_vars[i], onvalue=1, offvalue=0, bg='#168b8d', anchor='w')
        check.grid(row=i, column=0, sticky='nsew', padx=1, pady=1)

    # Filter Button
    button_filter = Button(frame_main, text='Фільтрувати', command=lambda: filter_treeview(columns, employee_rows, window, combos, gender_vars))
    button_filter.grid(row=1, column=4, padx=2, pady=2)
