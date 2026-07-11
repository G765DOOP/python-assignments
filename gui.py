from tkinter import *
import tkinter as tk
import time

window = Tk()
window.title("biscuit clicker: first gui in tkinter")



biscuit_amount= 0

#what happens when u click da biscuit
def biscuit_click():
    print("+1 biscuit")
    global biscuit_amount
    biscuit_amount += 1
    label.config(text = biscuit_amount)

#og biscuit
biscuit = Button(window, text="idk")
biscuit.config(command= biscuit_click)
biscuit_image = PhotoImage(file='image.png')
biscuit.config(image= biscuit_image )
biscuit.pack()





Worker_amount = 0
Worker = Button(window, text="2 biscuits: worker")
Worker.config(font=('Times New roman', 50))
Worker.config(state=tk.DISABLED)
Worker.pack()

def enable_worker_button():
    Worker.config(state=tk.NORMAL)

def worker_enable():
    if biscuit_amount >= 2:
        enable_worker_button

Worker.after(100, worker_enable)





#to know its biscuit clicker
label = Label(window, text = biscuit_amount)
label.config(font=('Monospace' , 50))
label.pack()



worker_enable()

window.mainloop()

