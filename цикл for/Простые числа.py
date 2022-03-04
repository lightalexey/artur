k=0
a=int(input('Введите целове число: '))
for i in range(1,a+1):
    if a%i==0:
        k += 1
if k == 2:
    print('Число',a ,'простое')
else:
    print('Число',a ,'составное')




