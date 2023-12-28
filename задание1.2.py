from tkinter import *
from tkinter import ttk


def getInfo():
    print('Имя: ', nameT.get())
    print('Фамилия: ', lastNameT.get())
    if polvar.get() == 'm':
        print('Пол: мужской')
    elif polvar.get() == 'w':
        print('Пол: женский')
    else:
        print('Пол не указан')
    print('Любимые предметы: ')
    if var1.get() == 1:
        print(' - математика')
    if var2.get() == 1:
        print(' - английский язык')
    if var3.get() == 1:
        print(' - информационные технологии')


window = Tk()
window.title('Регистрация')

name = Label(window, text = 'Имя', width = 20, height = 1, fg = 'blue', font = 'arial 18')
lastName = Label(window, text = 'Фамилия', width = 20, height = 1, fg = 'blue', font = 'arial 18')
pol = Label(window, text = 'Пол', width = 20, height = 1, fg = 'blue', font = 'arial 18')
likePr = Label(window, text = 'Любимые предметы', width = 20, height = 1, fg = 'blue', font = 'arial 18')

nameT = Entry(window, width = 30, font = 'arial 14')
lastNameT = Entry(window, width = 30, font = 'arial 14')

polvar = StringVar()
polvar.set(' ')
radio1 = Radiobutton(window, text = 'мужской', variable = polvar, value = 'm')
radio2 = Radiobutton(window, text = 'женский', variable = polvar, value = 'w')

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
check1 = Checkbutton(window, text = 'математика', variable = var1, onvalue = 1, offvalue = 0)
check2 = Checkbutton(window, text = 'английский язык', variable = var2, onvalue = 1, offvalue = 0)
check3 = Checkbutton(window, text = 'информационные технологии', variable = var3, onvalue = 1, offvalue = 0)

btn = Button(window, text = 'Принять', width = 25, height = 5, fg = 'blue', font = 'arial 14', command = getInfo)

name.pack()
nameT.pack()
lastName.pack()
lastNameT.pack()
pol.pack()
radio1.pack()
radio2.pack()
likePr.pack()
check1.pack()
check2.pack()
check3.pack()
btn.pack()

window.mainloop()
