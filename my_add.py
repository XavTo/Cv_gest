def valid_wh_ret(self, event, wh_fonc, entry, my_but, save_info, info):
        if (wh_fonc == 0):
            self.recup_entry_com(entry, my_but, save_info, info)
        if (wh_fonc == 1):
            self.recup_entry_spe(entry, my_but, save_info, info)
        if (wh_fonc == 2):
            self.recup_entry_date(entry, my_but, save_info, info)
        if (wh_fonc == 3):
            self.recup_entry_rep(entry, my_but, save_info, info)
        self.add_menu(info)

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