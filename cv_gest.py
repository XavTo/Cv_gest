import sys
import my_parser as p
import my_write as w
from tkinter import *
from functools import partial

def get_info():
    fd = open("info.json")
    ret = fd.read()
    fd.close
    info = p.my_parser(ret)
    return info

def init_window():
    window = Tk()
    window.title("CV GEST")
    window.geometry("1080x720")
    window.minsize(1080, 720)
    window.maxsize(1080, 720)
    window.iconbitmap('@logo.xbm')
    window.config(background='#a2fcff')
    return window

def add_menu(info):
    i = 0
    mymenu = Menu(window)
    ong_menu = Menu(mymenu, tearoff=0)
    del_menu = Menu(mymenu, tearoff=0)
    for element in info:
        del_menu.add_command(label=element[0], command=partial(my_delete_thing, info, i))
        i += 1
    ong_menu.add_command(label="Ajouter", command=lambda: my_create_thing(info))
    ong_menu.add_cascade(label="Supprimer", menu=del_menu)
    ong_menu.add_command(label="Quitter", command=window.quit)
    mymenu.add_cascade(label="Menu", menu=ong_menu)
    window.config(menu=mymenu)

def create_text():
    label_text = Label(window, text="Entreprise", font=("Arial, 20"), bg='#5eb7ba', fg='white')
    label_text.grid(row=0, column=0, ipadx=40)
    label_text = Label(window, text="Speciality", font=("Arial, 20"), bg='#5eb7ba', fg='white')
    label_text.grid(row=0, column=1, ipadx=40)
    label_text = Label(window, text="Date", font=("Arial, 20"), bg='#5eb7ba', fg='white')
    label_text.grid(row=0, column=2, ipadx=40)
    label_text = Label(window, text="Commentaire", font=("Arial, 20"), bg='#5eb7ba', fg='white')
    label_text.grid(row=0, column=3, ipadx=180)

def display_info(info):
    i = 1
    for element in info:
        label_text = Label(window, text=element[0], font=("Arial, 15"), bg='#ffea19', fg='black')
        label_text.grid(row=i, column=0)
        label_text = Label(window, text=element[1], font=("Arial, 15"), bg='#ffea19', fg='black')
        label_text.grid(row=i, column=1)
        label_text = Label(window, text=element[2], font=("Arial, 15"), bg='#ffea19', fg='black')
        label_text.grid(row=i, column=2)
        label_text = Label(window, text=element[3], font=("Arial, 15"), bg='#ffea19', fg='black')
        label_text.grid(row=i, column=3)
        i += 1

def valid_wh_ret(event, wh_fonc, entry, my_but, save_info, info):
    if (wh_fonc == 0):
        recup_entry_com(entry, my_but, save_info, info)
    if (wh_fonc == 1):
        recup_entry_spe(entry, my_but, save_info, info)
    if (wh_fonc == 2):
        recup_entry_date(entry, my_but, save_info, info)
    if (wh_fonc == 3):
        recup_entry_rep(entry, my_but, save_info, info)

def recup_entry_rep(rep_entry, my_but, info, old_info):
    window.unbind("<Return>")
    info[3] = rep_entry.get()
    my_but.grid_forget()
    rep_entry.grid_forget()
    old_info.append(info)
    w.write_info(old_info)
    info = get_info()
    display_info(info)
    add_menu(info)
    return None

def recup_entry_date(date_entry, my_but, info, old_info):
    window.unbind("<Return>")
    info[2] = date_entry.get()
    my_but.grid_forget()
    date_entry.grid_forget()
    rep_entry = Entry(window, font=("Arial"), bg='#ffea19', fg='Red')
    rep_entry.grid(column=3)
    my_but = Button(window, text="Valid", command=lambda: recup_entry_rep(rep_entry, my_but, info, old_info))
    window.bind("<Return>", lambda event: valid_wh_ret(event, 3, rep_entry, my_but, info, old_info))
    my_but.grid(column=3)
    return None

def recup_entry_spe(spe_entry, my_but, info, old_info):
    window.unbind("<Return>")
    info[1] = spe_entry.get()
    my_but.grid_forget()
    spe_entry.grid_forget()
    date_entry = Entry(window, font=("Arial"), bg='#ffea19', fg='Red')
    date_entry.grid(column=2)
    my_but = Button(window, text="Valid", command=lambda: recup_entry_date(date_entry, my_but, info, old_info))
    window.bind("<Return>", lambda event: valid_wh_ret(event, 2, date_entry, my_but, info, old_info))
    my_but.grid(column=2)
    return None

def recup_entry_com(company_entry, my_but, info, old_info):
    window.unbind("<Return>")
    info[0] = company_entry.get()
    spe_entry = Entry(window, font=("Arial"), bg='#ffea19', fg='Red')
    spe_entry.grid(column=1)
    my_but.grid_forget()
    company_entry.grid_forget()
    my_but = Button(window, text="Valid", command=lambda: recup_entry_spe(spe_entry, my_but, info, old_info))
    window.bind("<Return>", lambda event: valid_wh_ret(event, 1, spe_entry, my_but, info, old_info))
    my_but.grid(column=1)
    return None

def my_create_thing(info):
    save_info = ["", "", "", ""]
    company_entry = Entry(window, font=("Arial"), bg='#ffea19', fg='Red')
    company_entry.grid()
    my_but = Button(window, text="Valid", command=lambda: recup_entry_com(company_entry, my_but, save_info, info))
    my_but.grid()
    window.bind("<Return>", lambda event: valid_wh_ret(event, 0, company_entry, my_but, save_info, info))
    return None

def my_delete_thing(info, i):
    del info[i]
    w.write_info(info)
    for rem in window.winfo_children():
        rem.destroy()
    create_text()
    info = get_info()
    display_info(info)
    add_menu(info)

info = get_info()
window = init_window()
create_text()
display_info(info)
add_menu(info)
window.mainloop()