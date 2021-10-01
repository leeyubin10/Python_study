from tkinter import *
import tkinter.messagebox
window = Tk()

click = True

def btnClick(btns):
    global click
    if btns["text"] == "" and click == True:
        btns["text"] = "X"
        btns['bg'] = 'yellow'
        click = False
        checkForWin()
        
    elif btns["text"] == "" and click == False:
        btns["text"] = "O"
        btns['bg'] = 'green'
        click = True
        checkForWin()

def checkForWin():
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
        btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
        btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
        btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
        btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
        btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
        btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
        btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
        btn7['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):
        tkinter.messagebox.showinfo("틱택토","'X' is winner")

    elif (btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
          btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
          btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
          btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' or
          btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
          btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
          btn7['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):
        tkinter.messagebox.showinfo("틱택토","'O' is winner")


btns = StringVar()

btn1=Button(window, text="",width=10, command = lambda:btnClick(btn1))
btn1.grid(column=0, row=0)

btn2=Button(window, text="",width=10, command = lambda:btnClick(btn2))
btn2.grid(column=1, row=0)

btn3=Button(window, text="",width=10, command = lambda:btnClick(btn3))
btn3.grid(column=2, row=0)

btn4=Button(window, text="",width=10, command = lambda:btnClick(btn4))
btn4.grid(column=0, row=1)

btn5=Button(window, text="",width=10, command = lambda:btnClick(btn5))
btn5.grid(column=1, row=1)

btn6=Button(window, text="",width=10, command = lambda:btnClick(btn6))
btn6.grid(column=2, row=1)

btn7=Button(window, text="",width=10, command = lambda:btnClick(btn7))
btn7.grid(column=0, row=2)

btn8=Button(window, text="",width=10, command = lambda:btnClick(btn8))
btn8.grid(column=1, row=2)

btn9=Button(window, text="",width=10, command = lambda:btnClick(btn9))
btn9.grid(column=2, row=2)

window.mainloop()
