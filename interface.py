from tkinter import *
import main
root = Tk()
root.geometry("300x300")
summ = 'Введите сумму'
komm = 'По желанию, оставьте комментарий'
balance = main.balance()


def add(button):
    main.add_money(int(eSumma.get()), eKomm.get())
    lBalans['text'] = main.balance()


def remove(button):
    main.subtrack_money(int(eSumma.get()), eKomm.get())
    lBalans['text'] = main.balance()


bRashod = Button(root, text='расход')
bDohod  = Button(root, text='доход')
bGrafic = Button(root, text='график')
lBalans = Label(root, text=balance, width=40)
eSumma  = Entry(root, text=summ)
eKomm   = Entry(root, text=komm)

lBalans.place(relx=0, rely=0, relwidth=1, relheight=1/3.5)
eSumma.place(relx=0, rely=1/3.5, relwidth=1, relheight=1/7)
eKomm.place(relx=0, rely=3/7, relwidth=1, relheight=1/7)
bRashod.place(relx=0, rely=2/3.5, relwidth=0.5, relheight=1/7)
bDohod.place(relx=0.5, rely=2/3.5, relwidth=0.5, relheight=1/7)
bGrafic.place(relx=0, rely=6/7, relwidth=1, relheight=1/7)
bDohod.bind("<Button-1>", add)
bRashod.bind("<Button-1>", remove)
bGrafic.bind("<Button-1>", main.grafic)




root.resizable(False, False)






root.mainloop()

