"""
В-3. Задание №3.Найти интегральный гиперболический синус.
"""

import math
import sys

# Точность вычислений
EPS = 10 ** -10
# Вводим необходимую величину
if __name__ == '__main__':
    x = float(input("add value for x: "))
    if x == 0:
         print("Illegal value of x", file=sys.stderr)
         exit(1)

    a = x ** 3 / 18
    S, n = a, 1

    # Находим сумму членов ряда
    while math.fabs(a) > EPS:
         a *= (x ** (2*n+1) * n) / (2 * n + 1) ** 2 * x ** n
         S += a
         n += 1

    # Выводим значение
    print(f"Si({x}) = {x + S}")