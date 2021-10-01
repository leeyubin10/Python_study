from tkinter import *
from tkinter import messagebox

window = Tk()

def btn1_clicked():
    messagebox.showinfo('메시지 제목','안녕하세요 메시지 본문입니다')
def btn2_clicked():
    messagebox.showwarning('주의 메시지 제목','이 파일은 바이러스에 감염되었습니다')
def btn3_clicked():
    messagebox.showerror('에러 메시지','파일 오픈 에러')
def btn4_clicked():
    res = messagebox.askquestion('질문 메시지','예/아니오로 답하세요')
def btn5_clicked():
    res = messagebox.askyesno('질문 메시지','예/아니오로 답하세요')
def btn6_clicked():
    res = messagebox.askyesnocancel('질문 메시지','예/아니오/취소로 답하세요')
def btn7_clicked():
    res = messagebox.askokcancel('질문 메시지','확인/취소로 답하세요')
def btn8_clicked():
    res = messagebox.askretrycancel('질문 메시지','다시시도/취소로 답하세요')
    
btn1=Button(window, text='일반메시지', command = btn1_clicked)
btn1.grid(column=0, row=0)
btn2=Button(window, text='주의메시지', command = btn2_clicked)
btn2.grid(column=1, row=0)
btn3=Button(window, text='에러메시지', command = btn3_clicked)
btn3.grid(column=2, row=0)
btn4=Button(window, text='질문메시지 예/아니오', command = btn4_clicked)
btn4.grid(column=3, row=0)
btn5=Button(window, text='질문메시지 예/아니오', command = btn5_clicked)
btn5.grid(column=0, row=1)
btn6=Button(window, text='질문메시지 예/아니오/취소', command = btn6_clicked)
btn6.grid(column=1, row=1)
btn7=Button(window, text='질문메시지 확인/취소', command = btn7_clicked)
btn7.grid(column=2, row=1)
btn8=Button(window, text='질문메시지 다시시도/취소', command = btn8_clicked)
btn8.grid(column=3, row=1)

window.mainloop()
