"""
Из трех действительных чисел a,b и c выбрать те, модули которых не меньше 4.
"""

import sys


from math import fabs
# Вводятся 3 любых числа
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
# Идёт перебор значений, которые больше > 4
if __name__ == '__main__':
    if fabs(a) >= 4:
        print("a=",fabs(a))
    elif fabs(b) >= 4:
         print("b=",fabs(b))
    elif fabs(c) >= 4:
        print("c=",fabs(c))
    else:
        print("Нет необходимых чисел!", file=sys.stderr)
        exit(1)