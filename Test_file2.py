from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='#6DF873')
canv.pack(side=LEFT, fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']


def new_ball():
    '''Функция создает круг из 5 рандомных цветов( red, orange, green, blue).
    С случайным значением радиуса, с помощью rnd(randrange).Шарик появляется на 1000мс,
    далее выполняется функция вызова прямоугольника.'''
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 300)
    y = rnd(100, 300)
    r = rnd(30, 50)
    canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(1000, new_ball)


def ball_ball():
    global x1, y1, r, m, x2, y2, x3, y3
    canv.delete(ALL)
    m = rnd(1, 4)
    x1 = rnd(100, 300)
    y1 = rnd(100, 300)
    r = rnd(30, 50)
    x2 = rnd(100, 300)
    y2 = rnd(100, 300)
    x3 = rnd(100, 300)
    y3 = rnd(100, 300)
    if m == 1:
        ball_1 = canv.create_oval(x1 - r, y1 - r, x1 + r, y1 + r, fill=choice(colors), width=0)
    if m == 2:
        ball_1 = canv.create_oval(x1 - r, y1 - r, x1 + r, y1 + r, fill=choice(colors), width=0)
        ball_2 = canv.create_oval(x2 - r, y2 - r, x2 + r, y2 + r, fill=choice(colors), width=0)
    if m == 3:
        ball_1 = canv.create_oval(x1 - r, y1 - r, x1 + r, y1 + r, fill=choice(colors), width=0)
        ball_2 = canv.create_oval(x2 - r, y2 - r, x2 + r, y2 + r, fill=choice(colors), width=0)
        ball_3 = canv.create_oval(x3 - r, y3 - r, x3 + r, y3 + r, fill=choice(colors), width=0)
    root.after(1000, ball_ball)


x1 = rnd(100, 300)
y1 = rnd(100, 300)
r = rnd(30, 50)
x2 = rnd(100, 300)
y2 = rnd(100, 300)
x3 = rnd(100, 300)
y3 = rnd(100, 300)
ball_1 = canv.create_oval(x1 - r, y1 - r, x1 + r, y1 + r, fill=choice(colors), width=0)
ball_2 = canv.create_oval(x2 - r, y2 - r, x2 + r, y2 + r, fill=choice(colors), width=0)
ball_3 = canv.create_oval(x3 - r, y3 - r, x3 + r, y3 + r, fill=choice(colors), width=0)
points = 0


def motion():
    global x, ball_1
    canv.move(ball_1, -5, 0)
    if canv.coords(ball_1)[0] < 100:
        root.after(100, motion)
    root.after(100, new_ball)


def motion2():
    global y, ball_1
    canv.move(ball_1, 0, -5)
    if canv.coords(ball_1)[1] < 100:
        root.after(100, motion2)
    root.after(100, new_ball)


def click(event):
    global x1, y1, r, x2, y2, x3, y, points
    if event.x <= (x1 + r) and event.x >= (x1 - r):
        if event.y >= (y1 - r) and event.y <= (y1 + r):
            points += 1
            print('Попал')
            canv1.delete(ALL)
    if event.x <= (x2 + r) and event.x >= (x2 - r):
        if event.y >= (y2 - r) and event.y <= (y2 + r):
            points += 1
            print('Попал')
            canv1.delete(ALL)
    if event.x <= (x3 + r) and event.x >= (x3 - r):
        if event.y >= (y3 - r) and event.y <= (y3 + r):
            points += 1
            print('Попал')
            canv1.delete(ALL)
    text2 = canv1.create_text(60, 60, text=(points), font='Arial 20')


canv2 = Canvas(width=120, height=60, bg='white')
canv1 = Canvas(width=400, height=400, bg='white')
text = canv2.create_text(60, 20, text='Points', font='Arial 20')
canv.bind('<Button-1>', click)
canv2.pack(side=TOP)
canv1.pack(side=RIGHT)
motion()
motion2()
ball_ball()
mainloop()