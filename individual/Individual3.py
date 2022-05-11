"""
3.Начав тренировки, спортсмен пробежал 10 км. Каждый следующий день он увеличивал
дневную норму на 10% от нормы предыдущего дня. Какой суммарный путь пробежит
спортсмен за 7 дней?
"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-


dist = 0
day = 1
distance = 10

if __name__ == '__main__':
    while day < 7:
        distance += ((distance*10)/100)
        dist += distance
        day += 1
    print(dist)
