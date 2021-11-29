import codeGenerator
import template
import sys
import os
from template import *
from codeGenerator import *
from tkinter import *
from tkinter import colorchooser
import time


root = Tk()
root.title('Super Proga')
root.geometry("700x700")
f = open('code_' + time.strftime("%Y%m%d-%H%M%S") + '.txt', 'w')
f.write(template.header)
f.write(template.doubleEnter)

color = "black"
width = 40
lineStartX = 0
lineStartY = 0


def save():
    f.write(template.doubleEnter + template.doubleEnter + template.footer)
    f.close()
    time.sleep(1)
    python = sys.executable
    os.execl(python, python, *sys.argv)



def paint(event):
    global color, width
    # get x1, y1, x2, y2 co-ordinates
    x1, y1 = (event.x - 3), (event.y - 3)
    x2, y2 = (event.x + 3), (event.y + 3)

    # display the mouse movement inside canvas
    wn.create_oval(x1, y1, x2, y2, fill=color, outline=color, width=width)
    f.write(codeGenerator.paint(x1, y1, x2, y2, color, width))


def circle():
    global color, width
    wn.create_oval(
        x, y, x + width, y + width, width=width, fill=color, outline=color)
    f.write(codeGenerator.circle(x, y, color, width))


def square():
    global color, width
    wn.create_rectangle(
        x, y, x + 30, y + 30, width=width, fill=color, outline=color)
    f.write(codeGenerator.square(x, y, color, width))


def triangle():
    global color, width
    wn.create_polygon(
        x, y, x - (width * 2 / 2), y + width * 2, x + (width * 2 / 2), y + width * 2,
        fill=color, outline=color, width=5)
    f.write(codeGenerator.triangle(x, y, color, width))


def lineStart():
    global lineStartX, lineStartY
    lineStartX = x
    lineStartY = y


def lineEnd():
    global color, width
    wn.create_line(lineStartX, lineStartY, x, y, width=width, fill=color)
    f.write(codeGenerator.line(lineStartX, lineStartY, x, y, width, color))


def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)


def colorPicker():
    global color
    colorCode = colorchooser.askcolor(title="Choose color")
    color = colorCode[1]


def changeWidth():
    global width
    width = int(txt.get())


b1 = Button(text="Изменить цвет",
            width=15, height=3)
b1.config(command=colorPicker)

b2 = Button(text="Изменить толщину",
            width=15, height=3)
b2.config(command=changeWidth)

saveBTN = Button(text="Завершить",
              width=15, height=3)
saveBTN.config(command=save)

txt = Entry(root, width=20)
txt.insert(0, 5)

txt.pack()
b2.pack()
b1.pack()
saveBTN.pack()
wn = Canvas(root, width=700, height=700, bg='white')
wn.bind('<B1-Motion>', paint)
wn.bind("<Button-3>", popup)
menu = Menu(tearoff=0)
menu.add_command(label="Круг",
                 command=circle)
menu.add_command(label="Квадрат",
                 command=square)
menu.add_command(label="Треугольник",
                 command=triangle)
menu.add_command(label="Начало линии",
                 command=lineStart)
menu.add_command(label="Конец линии",
                 command=lineEnd)
wn.pack()
root.mainloop()
