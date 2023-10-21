from tkinter import *

window = Tk() 
window.title("Калькулятор индекса массы тела (ИМТ)")
window.geometry('400x300')
frame = Frame(
   window, 
   padx = 10,
   pady = 10 
)
date_lb = Label(
   frame,
   text="Введи, пожалуйста, дату рождения"
)
date_lb.grid(row=2, column=1)

date_tf = Entry(
   frame, 
)
date_tf.grid(row=2, column=2) 
frame.pack(expand=True) 

frame.mainloop()
