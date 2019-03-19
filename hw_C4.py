a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c
if d > 0:
    print(a + (d**(1/2))/2, a - (d**(1/2))/2)
if d == 0:
    print(a + (d**(1/2))/2)
else:
    print('Корней нет')
