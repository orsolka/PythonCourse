import random
n = random.randint(1,100)
m = int(input('Угадайте число от 1 до 100: '))
while m != n:
    if m > n:
        print('Загаданное число меньше')
        m = int(input('Попытайтесь ещё раз: '))
    if m < n:
        print('Загаданное число больше')
        m = int(input('Попытайтесь ещё раз: '))
if m == n:
    print('Поздравляем, Вы угадали!')
