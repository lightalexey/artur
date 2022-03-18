summa=0
a=int(input('Введите число '))
for i in range(1,a):
    if a%i==0:
        summa=summa+i
if a==summa:
    print('Число совершенное')
else:
    print('Число не является совершенным')

