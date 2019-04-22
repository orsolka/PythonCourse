from math import sin
import numpy as np
a = float(input('Введите левую границу интервала интегрирования '))
b = float(input('Введите правую границу интервала интегрирования  '))
N = int(input('Введите число разбиений '))
def f(x):
    return(sin(x))
def Integral(a, b, N):
    h = (b - a)/N
    sum = 0
    for i in range(0, N):        
        sum += f(a+i*h)
    otvet = h * sum
    return(otvet)
print('{:.8f}'.format(Integral(a, b, N)) + '\n')
