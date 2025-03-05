# 1
import datetime
import math


def multi(l):
    # оздаем строку с выражением умножения всех элементов списка
    M = '*'.join(map(str, l))
    return (eval(M), " ", M)


print(multi([1, 2, 3, 3]))

# 2


def calcletter(s):
    quantitya = 0
    quantityb = 0
    for i in s:
        if i.islower():
            quantitya += 1
        elif i.upper():
            quantityb += 1
    return (quantitya, quantityb)


a = 'AAAAAAA'
print(calcletter(a))

# 3


def palin(s):
    if list(s) == list(reversed(s)):
        return ("Yes it is")
    else:
        return ("No it is not")


a = 'pads'
print(palin(a))
# 4


def sqrt(num, milsek):
    delta = datetime.timedelta(milliseconds=milsek)
    end = datetime.datetime.now() + delta
    while datetime.datetime.now() < end:
        pass
    return (math.sqrt(num))


a = 25100
b = 2123
print("Square root of", a, "after", b, "miliseconds is", sqrt(a, b))
# 5


def determine(num, t):
    print(f'tuple #{num} is {all(t)}')


t1 = (True, True, True, True)
t2 = (True, True, False, True)

determine(1, t1)
determine(2, t2)
