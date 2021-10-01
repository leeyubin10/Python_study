import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="apple.png")

w = tk.Label(root, image=logo) .pack(side='right')

explanation = '파이썬은 GIF/PNG 파일형식을 지원합니다'

w2 = tk.Label(root, text=explanation)
root.mainloop()
