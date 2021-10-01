from tkinter import *
from tkinter import Menu

def create():
    print("생성")

def edit():
    print("수정")
    
window = Tk()

menu = Menu(window)

sub_menu = Menu(menu)
sub_menu.add_command(label='생성', command = create)
sub_menu.add_separator()
sub_menu.add_command(label='수정', command = edit)

menu.add_cascade(label='파일', menu=sub_menu)

window.config(menu=menu)

window.mainloop()

