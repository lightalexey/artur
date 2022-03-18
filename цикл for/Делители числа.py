f=0
a=int(input('Введите число '))
for i in range(1,a+1):
    if a%i==0:
        print(i)
        f+=1
print(f)