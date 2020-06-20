from tkinter import *
import main
from tkinter import messagebox
okno = Tk()
okno.geometry("700x500")
okno.resizable(width=False, height=False)
okno.title("Финансовый калькулятор")

def warn():
    a = messagebox.showwarning(title='предупреждение',message='Должно быть введено число.')

def add(button):
    val=eSumma.get()
    if val.isdecimal():
        val=int(val)
    else:
        warn()
        return
    main.add_money(val, eKomm.get())
    lBalans['text'] = main.balance()
    eSumma.delete(0, END)
    eKomm.delete(0, END)
    historyUpdate()


def remove(button):
    val = eSumma.get()
    if val.isdecimal():
        val = int(val)
    else:
        warn()
        return
    main.subtrack_money(val, eKomm.get())
    lBalans['text'] = main.balance()
    eSumma.delete(0, END)
    eKomm.delete(0, END)
    historyUpdate()

def historyUpdate(*args):
    lHistory=main.historyReturn()
    tHistory['state'] = NORMAL
    tHistory.delete(1.0, END)
    for i in lHistory:
        tHistory.insert(END,i[0]+' ')
        if i[1] == '+':
            tHistory.insert(END, 'доход: ')
        else:
            tHistory.insert(END, 'расход: ')
        tHistory.insert(END, str(i[2])+'\n')
        tHistory.insert(END,i[3]+'\n \n')
    tHistory['state'] = DISABLED

summ='Введите сумму'
komm='По желанию, оставьте комментарий'
tHistory=Text(okno)
lbl=Label(okno, text='Ваш баланс:')
bRashod=Button(okno, text='расход')
bDohod=Button(okno, text='доход')
bGrafic=Button(okno, text='график')
lBalans=Label(okno, text=main.balance(), font=("Tahoma", 50))
eSumma=Entry(okno,text=summ)
eKomm=Entry(okno,text=komm)

lbl.place(x=60,y=5,width=100,height=27)
tHistory.place(x=320,y=37,width=360, height=410)
lBalans.place(y=37,x=20,width=260, height=80)
eSumma.place(y=167,x=20,width=260, height=50)
eKomm.place(x=20,y=257,width=260, height=80)
bDohod.place(x=10,y=347,width=135, height=40)
bRashod.place(x=155,y=347,width=135, height=40)
bGrafic.place(x=100,y=417,width=100, height=50)

bDohod.bind("<Button-1>", add)
bRashod.bind("<Button-1>", remove)
bGrafic.bind("<Button-1>", main.grafic)
historyUpdate()


okno.mainloop()

# TODO вывод значений меньше range
# TODO подписи к окнам
# TODO sql таблица и insert