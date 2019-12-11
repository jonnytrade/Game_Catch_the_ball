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
    global x, y, r, z, ball
    c.delete(ALL)
    x = rnd(100,350)
    y = rnd(100,350)
    r = rnd(30,50)
    z = rnd(10,50)
    ball = c.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    if x>=300:
        c.move(ball,-z,0)
        print("BINGO",z)
    window.after(1000,new_ball)

def click(event):
    global x, y, r, point
    if event.y >= (y-r) and event.y <= (y+r):
        if event.x >= (x-r) and event.x <= (x+r):
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