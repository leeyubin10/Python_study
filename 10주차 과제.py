from tkinter import*
import pickle

window = Tk()

lb1 = Label(window, text='이름')
lb1.grid(row=0, column=0)
txt1 = Entry(window, width=30)
txt1.grid(row=0, column=1)
lb2 = Label(window, text='전화번호')
lb2.grid(row=1, column=0)
txt2 = Entry(window, width=30)
txt2.grid(row=1,column=1)

phone_book={}
n = 0

def btn1_clicked():
    name = str(txt1.get())
    tel = str(txt2.get())
    phone_book[name] = tel
    file = open("phone_book.dat","wb")
    pickle.dump(phone_book, file)
    file.close()
def btn2_clicked():
    txt1.delete(0,END)
    txt2.delete(0,END)
    file = open("phone_book.dat", "rb")
    obj = pickle.load(file)
    lst = list(obj.keys())
    lst2 = list(obj.values())
    txt1.insert(0,lst[0])
    txt2.insert(0,lst2[0])
def btn3_clicked():
    global n
    txt1.delete(0,END)
    txt2.delete(0,END)
    file = open("phone_book.dat", "rb")
    obj = pickle.load(file)
    lst = list(obj.keys())
    lst2 = list(obj.values())
    n+=1
    txt1.insert(0,lst[n])
    txt2.insert(0,lst2[n])
def btn4_clicked():
    global n
    txt1.delete(0,END)
    txt2.delete(0,END)
    file = open("phone_book.dat", "rb")
    obj = pickle.load(file)
    lst = list(obj.keys())
    lst2 = list(obj.values())
    n-=1
    txt1.insert(0,lst[n])
    txt2.insert(0,lst2[n])
def btn5_clicked():
    txt1.delete(0,END)
    txt2.delete(0,END)
    file = open("phone_book.dat", "rb")
    obj = pickle.load(file)
    lst = list(obj.keys())
    lst2 = list(obj.values())
    txt1.insert(0,lst[-1])
    txt2.insert(0,lst2[-1])
def btn6_clicked():
    global n
    file = open("phone_book.dat", "rb")
    obj = pickle.load(file)
    lst = list(obj.keys())
    lst2 = list(obj.values())
    txt1.insert(0,lst[n])
    txt2.insert(0,lst2[n])

btn1=Button(window, text='추가', width=15, command = btn1_clicked)
btn1.grid(row=2, column=0)
btn2=Button(window, text='처음', width=10,command = btn2_clicked)
btn2.grid(row=2, column=1)
btn3=Button(window, text='다음', width=10, command = btn3_clicked)
btn3.grid(row=2, column=2)
btn4=Button(window, text='이전', width=10, command = btn4_clicked)
btn4.grid(row=2, column=3)
btn5=Button(window, text='마지막', width=10, command = btn5_clicked)
btn5.grid(row=2, column=4)
btn6=Button(window, text='파일 읽기', width=10, command = btn6_clicked)
btn6.grid(row=2, column=5)

window.mainloop()
