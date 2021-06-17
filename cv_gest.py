import sys
import my_parser as p
from tkinter import *

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
    window.config(background='#a2fcff')
    return window

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

def my_create_thing():
    print("press")

info = get_info()
window = init_window()
create_text()
display_info(info)
cr_button = Button(window, text="create new cv", font=("Arial, 20"), bg='white', fg='#5eb7ba', command=my_create_thing)
cr_button.grid()
window.mainloop()