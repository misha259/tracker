import shelve
import time
import matplotlib.pyplot as plt
data = shelve.open("data")


def add_money(count,comm):
    t=time.strftime('%d %m %y %H %M %S')
    data[t]=['+',count,comm]

def subtrack_money(count, comm):
    t = time.strftime('%d %m %y %H %M %S')
    data[t] = ['-', count, comm]

def balance():
    res = 0
    for i in data:
        i_data = data[i]
        if i_data[0] == '-':
            res -= i_data[1]
        elif i_data[0] == '+':
            res += i_data[1]
    return res


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
        print(balance())
        inp = input('Введите команду: ').lower()
        continue
    if inp[0] =='график':
        val=dict()
        for key in data:
            v=data[key]
            if v[2] in val:
                if v[0]=='+':
                    val[v[2]]+=v[1]
                elif v[0]=='-':
                    val[v[2]] -= v[1]
            else:
                val[v[2]]=v[1]
        plt.pie(val.values(),labels=val.keys())
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