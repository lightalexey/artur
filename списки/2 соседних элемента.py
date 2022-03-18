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
a1=a[0]
a2=a[1]
in1=0
in2=1
for i in range(n-1):
    if a[i]+a[i+1]>a1+a2:
        a1=a[i]
        a2=a[i+1]
        in1=i
        in2=i+1
print(a1,a2)
print(in1,in2)