import shelve
import time
import matplotlib.pyplot as plt
data = shelve.open("data")


def save():
    global data
    data.close()
    data = shelve.open("data")


def add_money(count, comm):
    t = time.strftime('%d %m %y %H %M %S')
    data[t] = ['+', count, comm]
    save()


def subtrack_money(count, comm):
    t = time.strftime('%d %m %y %H %M %S')
    data[t] = ['-', count, comm]
    save()


def balance():
    res = 0
    for i in data:
        i_data = data[i]
        if i_data[0] == '-':
            res -= i_data[1]
        elif i_data[0] == '+':
            res += i_data[1]
    return res


def grafic(*args):
    add = dict()
    sub = dict()
    for key in data:
        v = data[key]
        if v[0] == '+':
            if v[2] in add:
                add[v[2]] += v[1]
            else:
                add[v[2]] = v[1]
    for key in data:
        v = data[key]
        if v[0] == '-':
            if v[2] in sub:
                sub[v[2]] += v[1]
            else:
                sub[v[2]] = v[1]
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.pie(add.values(), labels=add.keys())
    ax2.pie(sub.values(), labels=sub.keys())
    plt.show()


#интерфейс
inp = ''
while inp != 'выйти':
    if __name__ != '__main__':
        break
    inp=input('Введите команду: ').lower()
    inp=inp.split()

    if inp[0] == 'баланс':
        print(balance())
        continue

    if inp[0] =='график':
        grafic()
        continue

    if len(inp)<2:
        print("неполные данные")
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


if __name__ == '__main__':
    data.close()