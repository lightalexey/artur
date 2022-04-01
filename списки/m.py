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
maximum = a[0]
indexmaxsimum = 0
minimum = a[0]
indexminimum = 0
for i in range(n):
    if a[i] > maximum:
        maximum = a[i]
        indexmaxsimum = i
    if a[i]<minimum:
        minimum = a[i]
        indexminimum = i
print(minimum,indexminimum)
print(maximum, indexmaxsimum)
print(max(a))

