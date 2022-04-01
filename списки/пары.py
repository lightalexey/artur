from random import randrange
a = []
n = 6
print('Исходный заполненный список:')
for i in range(n):
    number = randrange(11)  # случайное число в [-50;50]
    a.append(number)
    print(a[i], end=' ')
print()
# код начинается отсюда...
print()
for i in range(n-1):
    if i%2==0:
        print(a[i],a[i+1])
print()
for i in range(0,n-1,2):
    print(a[i],a[i+1])