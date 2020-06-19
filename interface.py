from tkinter import *
import main
okno = Tk()
okno.geometry("300x500")
okno.resizable(width=False, height=False)
okno.title("Финансовый калькулятор")

summ='Введите сумму'
komm='По желанию, оставьте комментарий'
bRashod=Button(okno, text='расход')
bDohod=Button(okno, text='доход')
bGrafic=Button(okno, text='график')
lBalans=Label(okno, textvariable=main.balance(), font=("Tahoma", 50))
eSumma=Entry(okno,textvariable=summ)
eKomm=Entry(okno,textvariable=komm)

#добавить надпись ваш баланс
lBalans.place(y=37,x=20,width=260, height=80)
eSumma.place(y=167,x=20,width=260, height=50)
eKomm.place(x=20,y=257,width=260, height=80)
bDohod.place(x=10,y=347,width=135, height=40)
bRashod.place(x=155,y=347,width=135, height=40)
bGrafic.place(x=100,y=417,width=100, height=50)





# lBalans.grid(row = 1, column = 1,rowspan = 2, columnspan = 2)
# eSumma.grid(row = 3, column = 1, columnspan = 2)
# eKomm.grid(row = 4, column = 1, columnspan = 2)
# bDohod.grid(row = 5, column = 1)
# bRashod.grid(row = 5, column = 2)
# bGrafic.grid(row = 7, column = 1, columnspan = 2)













okno.mainloop()

