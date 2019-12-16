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

def new_ball():
    """
    Функция вызова шарика в рабочей области root с переменным цветом colors. Шарик появляется на
    1000 мс и потом исчезает. Координаты шарика выбираются рандомно с помощью функции randrange.
    """
    global x, y, r, z, m, x1, y1, r1, ball1, ball2
    c.delete(ALL)
    x = rnd(100, 350)
    y = rnd(100, 350)
    r = rnd(10, 30)
    r1 = rnd(10, 30)
    z = rnd(10, 30)
    m = rnd(1,3)
    x1 = rnd(100,300)
    y1 = rnd(100,350)
    if (x1-x)< 50: # Функция исключает совпадение двух целей по координатам
        x1=x-50
    if (y1-y)<50:
        y1=y-50
    if m==1:
        ball1 = c.create_oval(x-r, y-r, x+r, y+r, fill = choice(colors), width=0)
    if m==2:
        ball1 = c.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
        ball2 = c.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill=choice(colors), width=0)
    if c.coords(ball1)[2] > 330:
        motion_x()
    if c.coords(ball1)[3] > 330:
        motion_y()
    window.after(1000, new_ball)

def motion_x():
    """
    Функция смещает шарик влево от стены по оси X в случае если шарик появился рядом с правой стеной
    """
    global x, ball1
    c.move(ball1,-1,0)
    if c.coords(ball1)[2] > 300:
        window.after(10,motion_x)

def motion_y():
    """
    Функция смещает шарик вверх от нижней стены по оси Y, аналогично функции motion_x
    """
    global y, ball1
    c.move(ball1, 0, -1)
    if c.coords(ball1)[3] > 300:
        window.after(10,motion_y)


def click(event):
    """
    Функция click отвечает за попадание курсора мыши по цели в игровом поле и добавляет 1 (один)
    за попадание по шарику.
    """
    global x, y, r, point
    if event.y >= (c.coords(ball1)[1]) and event.y <= (c.coords(ball1)[3]):
        if event.x >= (c.coords(ball1)[0]) and event.x <= (c.coords(ball1)[2]):
            point+=1
            c.delete(ALL)
            lbl2.configure(text=point)
    if event.y >= (c.coords(ball2)[1]) and event.y <= (c.coords(ball2)[3]):
        if event.x >= (c.coords(ball2)[0]) and event.x <= (c.coords(ball2)[2]):
            point+=1
            c.delete(ALL)
            lbl2.configure(text=point)


lbl1=Label(window, text="Player", font=("Arial Bold",20))
lbl2=Label(window, text=point, font=("Arial",30))

frame = Frame(width=100, height=100, bg="", colormap="new")
frame.pack(side=LEFT, padx=100,)

lbl1.pack()
lbl2.pack()
new_ball()
c.bind('<Button-1>', click)
window.mainloop()