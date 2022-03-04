# a1 a2 a3
a = []
n = int(input('Введи количество элементов:'))
for i in range(n):
    number = int(input('Введи число:'))
    a.append(number)
print('Исходный заполненный список:')
for i in range(n):
    print(a[i], end=' ')
print()
print(a)