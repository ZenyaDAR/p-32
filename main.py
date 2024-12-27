from my_file import *
from tkinter import *
from tkinter import ttk

def main_window():
    root = Tk()
    root.title('Книгарня')
    icon = PhotoImage(file='images/free-icon-book-3330314.png')
    root.iconphoto(False,icon)
    screen_width = root.winfo_screenmmwidth()
    screen_height = root.winfo_screenheight()
    root.maxsize(10000,10000)
    window_width = int(screen_width*0.6)
    window_height = int(screen_height*0.6)
    root.geometry(f'{window_width}x{window_height}')
    root.minsize(400,600)
    root.config(bg = '#3ddee1')


    style = ttk.Style()
    style.configure('Treeview', rowheight=30, font=('Times New Roman', 12))
    style.configure('Treeview.Heading', rowheight=30,font=('Times New Roman', 12, "bold") )


    btn_frame = Frame(root, height=50, width=50, bg="#3ddee1")
    btn_frame.grid(row=0,column=0,sticky='nw')


    btn_book = Button(btn_frame,text="books", font = ('Times New Roman',12, 'bold'), command=lambda : load_book(tree,root,filter_frame))
    btn_book.grid(row=0, column=0, padx=2, pady=2)


    btn_employee_book = Button(btn_frame,text="Emploee", font = ('Times New Roman',12, 'bold'), command=lambda : load_employees(tree,root,filter_frame))
    btn_employee_book.grid(row=0, column=1, padx=2, pady=2)


    tr_frame = Frame(root,bg="#3ddee1")
    tr_frame.grid(row=2,padx=2,pady=2,sticky='nw')
    tree = ttk.Treeview(tr_frame, show='headings')
    tree.grid_remove()


    filter_frame = Frame(root, bg='#168b8d',pady=10)
    filter_frame.grid(row=3,column=0,sticky="nsew")


    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)

    root.mainloop()


if __name__ == '__main__':
    main_window()