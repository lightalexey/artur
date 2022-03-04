from random import randrange
a = []
n = 10
print('Исходный заполненный список:')
for i in range(n):
    number = randrange(101) - 50 # случайное число в [-50;50]
    a.append(number)
    print(a[i], end=' ')
print()
# код начинается отсюда...
summa = 0
k2 = 0
for i in range(n):
    summa += a[i]
    if a[i] % 2 == 0:
        k2 += 1

print('Сумма всех элементов массива равна', summa)
print('2 способ. Сумма всех элементов массива равна', sum(a))
print('Количество четных элементов:', k2)
