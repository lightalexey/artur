from random import randrange
a = []
n = 10
print('Исходный заполненный список:')
for i in range(n):
    number = randrange(-5,6)
    a.append(number)
    print(a[i], end=' ')
print()
# код начинается отсюда...
summa = 0
k2 = 0
p=1
sp=0
kp=0
x=0
for i in range(n):
    summa += a[i]
    if a[i] % 2 == 0:
        k2 += 1
    if a[i]!=0:
        p*=a[i]
    if a[i]>0:
        sp+=a[i]
        kp+=1
    if a[i]==0:
       x+=1
print('Сумма всех элементов массива равна', summa)
print('2 способ. Сумма всех элементов массива равна', sum(a))
print('Количество четных элементов:', k2)
print('Произведение всех элементов:',p)
sr=summa/n
print(sr)
print(sp,kp,sp/kp)
print(a[0],a[-1])
print(len(a))
print('количество нулей:',x)