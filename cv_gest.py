import sys
import my_parser as p
import my_write as w
from tkinter import *
from tkinter import ttk
from functools import partial

class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("CV GEST")
        self.window.geometry("1080x720")
        self.window.minsize(800, 400)
        self.window.iconbitmap('@logo.xbm')
        self.window.config(background=self.light_blue())
        self.frame = Frame(self.window, bg=self.light_blue())
        self.frame.pack(fill=BOTH, expand=True, side=LEFT)

        self.already_activ = 0
        info = self.get_info()
        self.create_text()
        self.display_info(info)
        self.add_menu(info)

    def light_blue(self):
        return '#a2fcff'

    def dark_blue(self):
        return '#5eb7ba'

    def get_info(self):
        fd = open("info.json")
        ret = fd.read()
        fd.close
        info = p.my_parser(ret)
        return info

    def add_menu(self, info):
        i = 0
        mymenu = Menu(self.window)
        ong_menu = Menu(mymenu, tearoff=0)
        del_menu = Menu(mymenu, tearoff=0)
        for element in info:
            del_menu.add_command(label=element[0], command=partial(self.my_delete_thing, info, i))
            i += 1
        ong_menu.add_command(label="Ajouter", command=lambda: self.my_create_thing(info))
        ong_menu.add_cascade(label="Supprimer", menu=del_menu)
        ong_menu.add_command(label="Quitter", command=self.frame.quit)
        mymenu.add_cascade(label="Menu", menu=ong_menu)
        self.window.config(menu=mymenu)

    def create_text(self):
        self.frame.grid_columnconfigure((0,1,2,3), minsize=50, weight=1)
        label_text = Label(self.frame, text="Entreprise", font=("Arial, 20"), bg=self.dark_blue(), fg='white')
        label_text.grid(row=0, column=0)
        label_text = Label(self.frame, text="Speciality", font=("Arial, 20"), bg=self.dark_blue(), fg='white')
        label_text.grid(row=0, column=1)
        label_text = Label(self.frame, text="Date", font=("Arial, 20"), bg=self.dark_blue(), fg='white')
        label_text.grid(row=0, column=2)
        label_text = Label(self.frame, text="Commentaire", font=("Arial, 20"), bg=self.dark_blue(), fg='white')
        label_text.grid(row=0, column=3)

    def display_info(self, info):
        i = 1
        for element in info:
            label_text = Label(self.frame, text=element[0], font=("Arial, 15"), bg=self.light_blue(), fg='black')
            label_text.grid(row=i, column=0)
            label_text = Label(self.frame, text=element[1], font=("Arial, 15"), bg=self.light_blue(), fg='black')
            label_text.grid(row=i, column=1)
            label_text = Label(self.frame, text=element[2], font=("Arial, 15"), bg=self.light_blue(), fg='black')
            label_text.grid(row=i, column=2)
            label_text = Label(self.frame, text=element[3], font=("Arial, 15"), bg=self.light_blue(), fg='black')
            label_text.grid(row=i, column=3)
            i += 1

    def valid_wh_ret(self, event, wh_fonc, entry, my_but, save_info, info):
        if (wh_fonc == 0):
            self.recup_entry_com(entry, my_but, save_info, info)
        if (wh_fonc == 1):
            self.recup_entry_spe(entry, my_but, save_info, info)
        if (wh_fonc == 2):
            self.recup_entry_date(entry, my_but, save_info, info)
        if (wh_fonc == 3):
            self.recup_entry_rep(entry, my_but, save_info, info)

    def recup_entry_rep(self, rep_entry, my_but, info, old_info):
        if (len(rep_entry.get()) == 0):
            return None
        self.window.unbind("<Return>")
        info[3] = rep_entry.get()
        my_but.grid_forget()
        rep_entry.grid_forget()
        old_info.append(info)
        w.write_info(old_info)
        info = self.get_info()
        self.display_info(info)
        self.add_menu(info)
        self.already_activ = 0
        return None

    def recup_entry_date(self, date_entry, my_but, info, old_info):
        if (len(date_entry.get()) == 0):
            return None
        if (w.check_if_valid(date_entry.get()) == 1):
            return None
        self.window.unbind("<Return>")
        info[2] = date_entry.get()
        my_but.grid_forget()
        date_entry.grid_forget()
        rep_entry = Entry(self.frame, font=("Arial"), bg=self.dark_blue(), fg='Black')
        rep_entry.grid(column=3)
        my_but = Button(self.frame, text="Valid", command=lambda: self.recup_entry_rep(rep_entry, my_but, info, old_info))
        self.window.bind("<Return>", lambda event: self.valid_wh_ret(event, 3, rep_entry, my_but, info, old_info))
        my_but.grid(column=3)
        return None

    def recup_entry_spe(self, spe_entry, my_but, info, old_info):
        if (len(spe_entry.get()) == 0):
            return None
        self.window.unbind("<Return>")
        info[1] = spe_entry.get()
        my_but.grid_forget()
        spe_entry.grid_forget()
        date_entry = Entry(self.frame, font=("Arial"), bg=self.dark_blue(), fg='Black')
        date_entry.grid(column=2)
        my_but = Button(self.frame, text="Valid", command=lambda: self.recup_entry_date(date_entry, my_but, info, old_info))
        self.window.bind("<Return>", lambda event: self.valid_wh_ret(event, 2, date_entry, my_but, info, old_info))
        my_but.grid(column=2)
        return None

    def recup_entry_com(self, company_entry, my_but, info, old_info):
        if (len(company_entry.get()) == 0):
            return None
        info[0] = company_entry.get()
        self.window.unbind("<Return>")
        my_but.grid_forget()
        company_entry.grid_forget()
        spe_entry = Entry(self.frame, font=("Arial"), bg=self.dark_blue(), fg='Black')
        spe_entry.grid(column=1)
        my_but = Button(self.frame, text="Valid", command=lambda: self.recup_entry_spe(spe_entry, my_but, info, old_info))
        self.window.bind("<Return>", lambda event: self.valid_wh_ret(event, 1, spe_entry, my_but, info, old_info))
        my_but.grid(column=1)
        return None

    def my_create_thing(self, info):
        if (self.already_activ == 1):
            return None
        save_info = ["", "", "", ""]
        company_entry = Entry(self.frame, font=("Arial"), bg=self.dark_blue(), fg='Black')
        company_entry.grid()
        my_but = Button(self.frame, text="Valid", command=lambda: self.recup_entry_com(company_entry, my_but, save_info, info))
        my_but.grid()
        self.window.bind("<Return>", lambda event: self.valid_wh_ret(event, 0, company_entry, my_but, save_info, info))
        self.already_activ = 1
        return None

    def my_delete_thing(self, info, i):
        del info[i]
        w.write_info(info)
        for rem in self.frame.winfo_children():
            rem.destroy()
        self.create_text()
        info = self.get_info()
        self.display_info(info)
        self.add_menu(info)

app = MyApp()
app.window.mainloop()