from calendar import c
from tkinter import *
import random
import tkinter
win = tkinter.Tk()

win.geometry("1520x800")
win.title("자리 배정")
win.config(bg='white')


label = Label(win, text='배정')
label.pack(pady=10)
label.config(fg="gray", bg='black')

win.mainloop()

res = ''
n = 0
a = []

name = input("학생이름을 ,로 구분하여 적으세요 : ")
a.extend(name.split(','))
def rand():

    global res, n, a
   
    if n == 0 or n == 25:
        res = ''
        n = 0
        random.shuffle(a)
        print(a)
        res += a[n] + '     '
        n += 1
    
    if 0 <= n <=4 :
        res += a[n] + '     '
        if n == 4:
            res = res.strip() + '\n\n'
        n += 1

    if 5 <= n <=9 :
        res += a[n] + '     '
        if n == 9:
            res = res.strip() + '\n\n'
        n += 1
    if 10 <= n <=14 :
        res += a[n] + '     '
        if n == 14:
            res = res.strip() + '\n\n'
        n += 1
    if 15 <= n <=19 :
        res += a[n] + '     '
        if n == 19:
            res = res.strip() + '\n\n'
        n += 1
    if 20 <= n <=24 :
        res += a[n] + '     '
        if n == 24:
            res = res.strip() + '\n\n'
        n += 1
    if n == 25:
        res = res.strip()
    btn = Button(win, text='교탁')
    btn.config(width=13, height=2)
    btn.config(command=rand, fg="white", bg='black')
    btn.pack(pady=40)
    
    label.config(text=res)
