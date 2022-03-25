from random import randrange
a = []
n = 10
print('Исходный заполненный список:')
for i in range(n):
    number = randrange(11) # случайное число в [-50;50]
    a.append(number)
    print(a[i], end=' ')
print()
# код начинается отсюда...
in1=0
for i in range(n-1):
    if a[i]+a[i+1]>a[in1]+a[in1+1]:
        in1=i
print(a[in1],a[in1+1])
print(in1,in1+1)