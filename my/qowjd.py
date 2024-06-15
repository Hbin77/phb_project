from calendar import c
from tkinter import *
import random
import tkinter
win = tkinter.Tk()


win.geometry("1520x800")
win.title("자리 배정")
win.option_add("*Font", "양재블럭체 38")
win.config(bg='black')


e= Entry(win, width=20 )
e.pack()
e.insert(0,"학생 수를 입력")

res = ''
n = 0
a = ['김동민', '김주영', '문경호', '박경득', '박승원', '박정열', '박현빈', '박형우', '오승빈', '신동현', '조영창', '유원상', '윤유빈', '이동건', '이동호', '이동희', '이민혁', '이수환', '이임창', '이찬규', '이현우', '정재욱', '조영준', '오지율', '채희관']

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
    
    label.config(text=res)

btn = Button(win, text='교탁')
btn.config(width=13, height=2)
btn.config(command=rand, fg="blue", bg='black')
btn.pack(pady=40)

label = Label(win, text='배정')
label.pack(pady=10)
label.config(fg="yellow", bg='black')

win.mainloop()