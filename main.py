import shelve
import time
data = shelve.open("data")


def add_money(count,comm):
    t=time.strftime('%d %m %y %H %M %S')
    data[t]=['+',count,comm]

def subtrack_money(count, comm):
    t = time.strftime('%d %m %y %H %M %S')
    data[t] = ['-', count, comm]

#def balance:




#интерфейс
inp=''
inp=input('Введите команду: ').lower()
while inp != 'выйти':
    inp=inp.split()
    if len(inp)<2 and inp[0]!='баланс':
        print("неполные данные")
        inp = input('Введите команду: ').lower()
        continue
    if inp[0] == 'баланс':
        print(data)
        inp = input('Введите команду: ').lower()
        continue
    if inp[1].isdecimal():
        inp[1]=int(inp[1])
    else:
        print('неверный формат ввода')
        continue
    if inp[0] == 'доход':
        if len(inp)>2:
            comm = inp[2:]
            comm = ' '.join(comm)
            add_money(inp[1],comm)
        else:
            add_money(inp[1],'')
    if inp[0] == 'расход':
        if len(inp)>2:
            comm = inp[2:]
            comm = ' '.join(comm)
            subtrack_money(inp[1],comm)
        else:
            subtrack_money(inp[1],'')

    inp = input('Введите команду: ').lower()
data.close()