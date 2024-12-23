def adjust_window_size(win, tree):
    tree.update_idletasks()
    width = sum(tree.column(c, option='width') for c in tree['columns'])
    height = tree.winfo_reqheight()
    win.geometry(f"{width}x{height}")

def show_tree(columns, rows, win):
    for row in win.get_children():
        win.delete(row)
    
    win['columns'] = columns

    for column in columns:
        win.heading(column, text=column)
        win.column(column, anchor='center')

    for row in rows[1:]:
        win.insert('','end',values=row)
    win.grid()

def list_combo(my_list, index):
    v = list(set([my_list[i][index] for i in range(1, len(my_list))]))

    return v