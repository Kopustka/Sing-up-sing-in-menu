import tkinter as tk
from tkinter import *

from funcs_for_checking_punctuation import (сhecking_correctness_of_login,
                                            checking_correctness_of_password)

from classes1 import User

window = tk.Tk()
window.title('Регистрация/Вход')
window.geometry('650x350')

user_data= []

txt_log = None
txt_pass = None

frame_reg = tk.Frame(window)
frame_log = tk.Frame(window)

#functions

def get_usrname_password():
    res1 = "{}".format(txt_log.get())
    res2 = "{}".format(txt_pass.get())
    if res1 == '' or res2 == '':
        pass
    else:
        return [res1, res2]


def on_submit_reg():
    global user_data
    user_data = get_usrname_password()

    user_data[0] = сhecking_correctness_of_login(user_data[0])
    user_data[1] = checking_correctness_of_password(user_data[1])


    if any(not item for item in user_data):
        pass
    else:
        User.registration(user_data[0], user_data[1])

    print(user_data)



def on_submit_log():
    global user_data
    user_data = get_usrname_password()
    print(user_data)

    User.logining(user_data[0],user_data[1])


def clear_frames():
    frame_reg.forget()
    frame_log.forget()



def reg_frame():
    clear_frames()
    frame_reg.pack(expand=True, fill='both')

    for widget in frame_reg.winfo_children():
        widget.destroy()

    tk.Label(frame_reg, text='Регистрация').pack(pady=10)

    global txt_log, txt_pass
    tk.Label(frame_reg, text='Логин').pack(pady=6)
    txt_log = Entry(frame_reg, width=30)
    txt_log.pack(pady=5)
    tk.Label(frame_reg, text='Пароль').pack(pady=6)
    txt_pass = Entry(frame_reg, width=30)
    txt_pass.pack(pady=5)

    tk.Button(frame_reg, text='Подтвердить', command=on_submit_reg).pack(pady=20)




def log_frame():
    clear_frames()
    frame_log.pack(expand=True, fill='both')

    for widget in frame_log.winfo_children():
        widget.destroy()

    tk.Label(frame_log, text='Войти').pack(pady=10)

    global txt_log, txt_pass
    tk.Label(frame_log, text='Логин').pack(pady=6)
    txt_log = Entry(frame_log, width=30)
    txt_log.pack(pady=5)
    tk.Label(frame_log, text='Пароль').pack(pady=6)
    txt_pass = Entry(frame_log, width=30)

    txt_pass.pack(pady=5)

    tk.Button(frame_log, text='Подтвердить', command=on_submit_log).pack(pady=20)


# --- Главное меню ---
frame_menu = tk.Frame(window, bg='lightblue')
frame_menu.pack(side='top', fill='x', pady=10)

tk.Button(frame_menu, text='Регистрация', command=reg_frame).pack(side='left', padx=10)
tk.Button(frame_menu, text='Вход', command=log_frame).pack(side='left', padx=10)

window.mainloop()



