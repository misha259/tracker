from tkinter import *
import main
root = Tk()
root.geometry("300x500")
summ='Введите сумму'
komm='По желанию, оставьте комментарий'
bRashod=Button(root, text='расход')
bDohod=Button(root, text='доход')
bGrafic=Button(root, text='график')
lBalans=Label(root, textvariable=main.balance())
eSumma=Entry(root,textvariable=summ)
eKomm=Entry(root,textvariable=komm)

lBalans.grid(row = 1, column = 1,rowspan = 2, columnspan = 2)
eSumma.grid(row = 3, column = 1, columnspan = 2)
eKomm.grid(row = 4, column = 1, columnspan = 2)
bDohod.grid(row = 5, column = 1)
bRashod.grid(row = 5, column = 2)
bGrafic.grid(row = 7, column = 1, columnspan = 2)









root.mainloop()

