from tkinter import *

window = Tk()

selected = IntVar()

def clicked():
    selection = selected.get()
    if selection == 1:
        img = PhotoImage(file='apple.png')
    elif selection == 2:
        img = PhotoImage(file='orange.png')
    elif selection == 3:
        img = PhotoImage(file='strawberry.png')
    elif selection == 4:
        img = PhotoImage(file='banana.png')
    imglabel.configure(image=img)
    imglabel.image = img

btn = Button(window, text='선택', command=clicked)

rd1 = Radiobutton(window, text='사과', value=1, variable=selected)
rd2 = Radiobutton(window, text='오렌지', value=2, variable=selected)
rd3 = Radiobutton(window, text='딸기', value=3, variable=selected)
rd4 = Radiobutton(window, text='바나나', value=4, variable=selected)

imglabel = Label(window, image='')
imglabel.grid(column=0, row=1)

rd1.grid(column=0, row=0)
rd2.grid(column=1, row=0)
rd3.grid(column=2, row=0)
rd4.grid(column=3, row=0)
btn.grid(column=4, row=0)

window.mainloop()
