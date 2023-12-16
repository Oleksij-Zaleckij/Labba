from tkinter import *
root = Tk()

def btn_click():
    print("привіт")

root['bg'] = '#fafafa'
root.title('Назва програми')
root.wm_attributes('-alpha', 10)
root.geometry('500x500')

canvas = Canvas(root, height=300, width=250)
canvas.pack()
frame = Frame(root, bg='black')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
title = Label(frame, text='текст', bg='white', font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg='white', command=btn_click)
btn.pack()

root.resizable(width=False, height=False)
root.mainloop()
#кнопка на тк кінтері щоб виводити текст в термінал
