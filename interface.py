from tkinter import *
import main
okno = Tk()
okno.geometry("300x500")
okno.resizable(width=False, height=False)
okno.title("Финансовый калькулятор")


def add(button):
    main.add_money(int(eSumma.get()), eKomm.get())
    lBalans['text'] = main.balance()
    eSumma.delete(0, END)
    eKomm.delete(0, END)


def remove(button):
    main.subtrack_money(int(eSumma.get()), eKomm.get())
    lBalans['text'] = main.balance()
    eSumma.delete(0, END)
    eKomm.delete(0, END)


summ='Введите сумму'
komm='По желанию, оставьте комментарий'
lbl=Label(okno, text='Ваш баланс:')
bRashod=Button(okno, text='расход')
bDohod=Button(okno, text='доход')
bGrafic=Button(okno, text='график')
lBalans=Label(okno, text=main.balance(), font=("Tahoma", 50))
eSumma=Entry(okno,text=summ)
eKomm=Entry(okno,text=komm)

lbl.place(x=60,y=5,width=100,height=27)
lBalans.place(y=37,x=20,width=260, height=80)
eSumma.place(y=167,x=20,width=260, height=50)
eKomm.place(x=20,y=257,width=260, height=80)
bDohod.place(x=10,y=347,width=135, height=40)
bRashod.place(x=155,y=347,width=135, height=40)
bGrafic.place(x=100,y=417,width=100, height=50)

bDohod.bind("<Button-1>", add)
bRashod.bind("<Button-1>", remove)
bGrafic.bind("<Button-1>", main.grafic)



okno.mainloop()

