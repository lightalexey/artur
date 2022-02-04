a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a<c+b :
    if c<b+a:
        if b<a+c:
            print('Треугольник построить можно')
        else:
            print('Треугольнк построить нельзя')
    else:
        print('Треугольнк построить нельзя')
else:
    print('Треугольнк построить нельзя')

