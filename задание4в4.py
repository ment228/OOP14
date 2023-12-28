from tkinter import *
from tkinter import ttk
import math
def tabulate():
    #значения параметра для табулирования
    start = 0.01
    end = 0.9
    step = 0.01

    total_steps = int((end - start) / step) + 1#общее количество шагов

    pb.config(maximum=total_steps, value=0)#установка значений для прогрессбара
    for i in range(total_steps):
        #вычисление значения функции
        x = start + i * step
        y = 2.5 + math.sin(-x)

        #добавление значения в список
        listbox.insert(END, f"x = {x}                                  |                                y = {y}")
        #увеличение значения прогрессбара
        pb.step()
def start():
    #функция которая запускает табулирование
    start_btn.config()
    tabulate()
window = Tk()
window.geometry("300x250")#разрешение окна

pb = ttk.Progressbar(window,length=150,)# Создание виджета прогрессбара

listbox = Listbox(window, width=50)#создание виджета списка

start_btn = Button(window, text="Расчет", command=start)

start_btn.pack()
listbox.pack()
pb.pack()
#размещение виджетов

window.mainloop()#завершение