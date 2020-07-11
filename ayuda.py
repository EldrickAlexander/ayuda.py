__author__ = 'Eldrick Alexander'

import tkinter as tk
from tkinter import *
from tkinter import messagebox, Tk
from tkinter.ttk import *
import time
import datetime


y = 0
div = 10    # Número de divisiones del 100%
c = 0       # Contador
unit = 0    # Estado de la iluminación 0-100


def horario():
#     global tDespertar
#     global tiempoActual

# NO FUNCIONA

#     tiempoActual = time2
#     print(tiempoActual)
    if y == 0:
        tDespertar = '19:53:00' # <--Al cumplir esta hora incrementa la ProgressBar

        if tDespertar == tiempoActual:
            # Incremento
            global div
            global c
            global unit
            if unit == 0:
                for i in range(div):
                    c += 1
                    unit = c/div*100
                    pbar['value'] = unit
                    time.sleep(1)
                    win.update()
        horarios['text'] = 'Hora de despertar: 7 am.'
        win.update()



# -----------------------------------------------------------------------------
cuenta = 0
year = datetime.datetime.today().year
month = datetime.datetime.today().month
tiempoActual = ''

def tick(time1=''):
    # Obtiene la hora actual del PC
    global cuenta
    global tDespertar

    # timePrueba = '17:29:00'
    time2 = time.strftime("%H:%M:%S")

    if time2 != time1:
        time1 = time2
        # tiempoActual = time2
        clock.config(text=time2)
        # print(tiempoActual)  

    clock.after(1000, tick) # Revisión cada segundo  



# -----------------------------------------------------------------------------
# INTERFAZ GRÁFICA

win = tk.Tk()
win.title('App v1.0')

win.attributes('-fullscreen', True)
win.bind('<F11>', lambda event: win.attributes("-fullscreen", not win.attributes("-fullscreen")))
win.bind("<Escape>", lambda event: win.attributes("-fullscreen", False))


f1 = tk.Frame(win)
f1.place(relx=.05, rely=.05, relwidth=.26, relheight=.08)
clock = tk.Label(f1, font=('Castellar',64), bg='black', fg='white')
clock.place(relwidth=1, relheight=1)
tick()


f31 = tk.Frame(win)
f31.place(relx=.7, rely=.05, relwidth=.25, relheight=.08)
horarios = tk.Label(f31, text='HORARIO', font=('Bahnschrift SemiBold SemiConden', 21), 
                    bg='black', fg='white', justify=tk.LEFT)
horarios.place(relwidth=1, relheight=1)
horario()


f4 = tk.Frame(win)
f4.place(relx=.7, rely=.14, relwidth=.25, relheight=.03)
# estilo = Style()
# estilo.configure('Fondo', bg='black')
pbar = Progressbar(
        f4,
        length = 200, 
        orient = HORIZONTAL,
        maximum = 100,
        value = 0,
        # style='Fondo',
        mode = 'determinate'
        )
pbar.place(relwidt=1, relheight=1)



win.mainloop()
