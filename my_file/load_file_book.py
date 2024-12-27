from my_file.file_show import load_file_csv
from tkinter import *
from tkinter import ttk
from treeview import *

def validate_float(text):
    try:
        if text == "":
            return True
        float(text)
        return True
    except ValueError:
        return False


def fillter_trewiew(colums, rows, win, combo, varCh, genres, scale, entries):
    selected_publisher = combo[0].get()
    selected_authors = combo[1].get()
    s = scale.get()
    selected_genres = []
    for var, genre in zip(varCh,genres):
        if var.get() == 1:
            selected_genres.append(genre)

    par = ''
    maxPrice = max(list_combo(rows, 3))
    line = []
    for i, entry in enumerate(entries):
        line.append(entry.get())
    if line[0] == '' and line[1] != '':
        minP = 0
        maxP = float(line[1])
    elif line[0] != '' and line[1] == '':
        minP = float(line[0])
        maxP = float(maxPrice)
    elif line[0] != '' and line[1] != '':
        minP = float(line[0])
        maxP = float(line[1])
    else:
        par = 'Усі'
    

    for item in win.get_children():
        win.delete(item)

    
    win['columns'] = colums
    for column in colums:
        win.heading(column, text=column)
        win.column(column, anchor='center')
    
    for row in rows[1:]:
        if (selected_publisher == "Усі" or row[2] == selected_publisher) and (selected_authors == "Усі" or row[-1] == selected_authors) and int(row[4]) <= s and (len(selected_genres) == 0 or row[1] in selected_genres) and (par == 'Усі' or minP <=  float(row[3]) <= maxP):
            win.insert("",'end',values=row)
    
    win.grid()


def load_book(w,r,fr_frame):
    clear_frame(fr_frame)
    fr_frame.grid()
    csv_file = "data/Books.csv"
    my_row = load_file_csv(csv_file)
    publisher = list_combo(my_row,2)
    genre = sorted(list_combo(my_row,1))
    author = list_combo(my_row,-1)
    list_count = list(map(int,list_combo(my_row,4)))
    minCount = min(list_count)
    maxCount = max(list_count)
    step = (maxCount - minCount) // 10

    my_column = ['Назва книги','Жанp','Видавництво','Ціна','Кількість','Дата',"Автор"]
    show_tree(my_column,my_row,w)
    adjust_window_size(r, w)
    w.grid_rowconfigure(0, weight=1)
    w.grid_columnconfigure(0, weight=1)



    label1 = Label(fr_frame,text='Видавництва', background='#168b8d')
    label1.grid(row=0, column=0, sticky='nw', padx=1, pady=1)
    combo1 = ttk.Combobox(fr_frame, values=["Усі"] + publisher, state='readonly')
    combo1.set('Усі')
    combo1.grid(row=0, column=1, sticky='nw', padx=1,pady=1)


    label2 = Label(fr_frame,text='Автор', background='#168b8d')
    label2.grid(row=1, column=0, sticky='nw', padx=1, pady=1)
    combo2 = ttk.Combobox(fr_frame, values=["Усі"] + author, state='readonly')
    combo2.set('Усі')
    combo2.grid(row=1, column=1,sticky='nw', padx=1,pady=1)

    combo_list = tuple([combo1, combo2])

    label3 = Label(fr_frame,text='Жанр', background='#168b8d')
    label3.grid(row=0, column=2, sticky='nw', padx=1, pady=1)

    cframe = Frame(fr_frame, bg='#168b8d')
    cframe.grid(row=0,column=3, rowspan=5, sticky='nsew', padx=1, pady=1)
    genre = sorted(genre)
    l = len(genre)
    list_var = ['var' + str(i) for i in range(1, l + 1)]
    for i in range(l):
        list_var[i] = IntVar()
        check = Checkbutton(cframe, text=genre[i], variable=list_var[i], onvalue=1, offvalue=0, bg='#168b8d', anchor='w')
        check.grid(row=i, column=1, sticky='nsew', padx=1, pady=1)


    scale1 = Scale(fr_frame, orient=HORIZONTAL, length=600, from_=minCount, to=maxCount, tickinterval=step, resolution=1)
    scale1.grid(row=0, column=4, padx=1, pady=1)
    scale1.set(maxCount)

    frame_price = Frame(fr_frame, bg='#168b8d')
    frame_price.grid(row=0, column=6, padx=1, pady=1)
    for c in range(2): fr_frame.grid_columnconfigure(c, weight=1)
    for r in range(2): fr_frame.grid_rowconfigure(r, weight=1)



    label4 = Label(frame_price, text='Вкажіть ціну',  bg='#168b8d')
    label4.grid(row=0, column=0, columnspan=2, padx=1, pady=1)

    list_entry = []
    vcmd = (frame_price.register(validate_float), "%P")
    for i in range(2):
        entry = Entry(frame_price, justify='center', validate="key", validatecommand=vcmd)
        entry.grid(row=1, column=i, padx=1, pady=1)
        list_entry.append(entry)
    
    button_filter = Button(fr_frame,text='Фільтрувати', command=lambda: fillter_trewiew(my_column, my_row, w, combo_list, list_var, genre, scale1, list_entry))
    button_filter.grid(row=1, column=4, padx=2, pady=2)