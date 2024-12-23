from tkinter import *
from my_file import *
from tkinter import messagebox
from main import main_window

def login():
    username = entry_log.get()
    password = entry_pass.get()

    if username != '' and password != '':
        data = (username, password)
        my_user = load_file('data/users.txt')
        if data in my_user:
            messagebox.showinfo('Login', f'You login {username}')
            entry_log.delete(0,END)
            entry_pass.delete(0,END)
            login_window.destroy()
            main_window()
        else:
            messagebox.showerror('Error',"Такого юзера не існує")
            entry_log.delete(0,END)
            entry_pass.delete(0,END)
    else:
        messagebox.showerror('Error',"Поля пусті")

def register():
    username = entry_log.get()
    password = entry_pass.get()

    if username != '' and password != '':
        data = (username, password)
        my_user = load_file('data/users.txt')
        usernames = [user[0] for user in my_user]
        if username not in usernames:
            write_file('data/users.txt', data)
            entry_log.delete(0,END)
            entry_pass.delete(0,END)
            messagebox.showinfo('Login', f'You register {username}')
        else:
            messagebox.showerror('Error',"Такий username вже є")
    else:
        messagebox.showerror('Error',"Поля пусті")
        


login_window = Tk()
login_window.title("Авторизація")
login_window.geometry("300x200+200+200")
login_window.config(bg="lightblue")
icon_photo = PhotoImage(file='images/free-icon.png')
login_window.iconphoto(False,icon_photo)


label_log = Label(login_window,text = 'Username:', font = ('Times New Roman',14,'bold'),bg = "lightblue")
label_log.grid(row = 0, column = 0, sticky='nw', padx = 10, pady = 10)
entry_log = Entry(login_window, font = ('Times New Roman',14), justify = 'center')
entry_log.grid(row = 1, column = 0, columnspan = 2,padx = 10, pady = 10, sticky = 'ew')


label_pass = Label(login_window,text = 'Password:', font = ('Times New Roman',14,'bold'),bg = "lightblue")
label_pass.grid(row = 2, column = 0, sticky='nw', padx = 10, pady = 10)
entry_pass = Entry(login_window, font = ('Times New Roman',14), justify= 'center', show = '*')
entry_pass.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = 'ew')


for c in range(2): login_window.columnconfigure(c, weight = 1)


btn_login = Button(login_window, text = "Login", command = login)
btn_login.config(bg = 'lightyellow', activebackground = "yellow")
btn_login.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 20, sticky = 'ew')

btn_register = Button(login_window, text = "Register", command = register)
btn_register.config(bg = 'lightyellow', activebackground = "yellow")
btn_register.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 0, sticky = 'ew')



login_window.mainloop()