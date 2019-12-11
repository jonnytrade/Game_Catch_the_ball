from tkinter import *
from random import randrange as rnd, choice
import time
window = Tk()
window.geometry("800x400")
window.title("Игра - Поймай шарик")

c=Canvas(window, width=400, height=400, bg="white")
c.pack(side=LEFT)
colors = ['red','orange','yellow','green','blue']
point=0
n=0
def new_ball():
    """
    Функция вызова шарика в рабочей области root с переменным цветом colors. Шарик появляется на
    1000 мс и потом исчезает. Координаты шарика выбираются рандомно с помощью функции randrange.
    """
    global x, y, r, z, m, x1, y1, r1, n, ball1, ball2
    c.delete(ALL)
    x = rnd(100, 350)
    y = rnd(100, 350)
    r = rnd(10, 50)
    r1 = rnd(10, 50)
    z = rnd(10, 30)
    m = rnd(1,3)
    x1 = rnd(100,300)
    y1 = rnd(100,350)
    if (x1-x)< 50:
        x1=x-50
    if (y1-y)<50:
        y1=y-50
    if m==1:
        ball1 = c.create_oval(x-r, y-r, x+r, y+r, fill = choice(colors), width=0)
    if m==2:
        ball1 = c.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
        ball2 = c.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill=choice(colors), width=0)
    window.after(500, new_ball)

def motion_x():
    global x, ball1
    while c.coords(ball1)[2] >250:
        c.move(ball1,-10,0)

def motion_y():
    global y, ball1
    c.move(ball1, 0, -1)
    if c.coords(ball1)[1] > 200:
        window.after(100,motion_y)
    window.after(100, new_ball)


def click(event):
    global x, y, r, point
    if event.y >= (y-r) and event.y <= (y+r):
        if event.x >= (x-r) and event.x <= (x+r):
            print("WOW")
            point+=1
            print(point)
            c.delete(ALL)
            lbl2.configure(text=point)
    if event.y >= (y1-r) and event.y <= (y1+r):
        if event.x >= (x1-r) and event.x <= (x1+r):
            print("WOW")
            point+=1
            print(point)
            c.delete(ALL)
            lbl2.configure(text=point)
    else:
        print("LOL")

lbl1=Label(window, text="Player", font=("Arial Bold",20))
lbl2=Label(window, text=point, font=("Arial",30))


lbl1.pack()
lbl2.pack()
new_ball()
c.bind('<Button-1>', click)
window.mainloop()