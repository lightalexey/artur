a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a<c+b and b<c+a and c<b+a:
   #print('Треугольник построить можно')
    if a==b==c:
        print('Треугольник равносторонний')
    else:
        if a==b or b==c or a==c:
            print('Треугольник равнобедренный')
        else:
            if c**2==a**2+b**2 or a**2==c**2+b**2 or b**2==a**2+c**2:
                print('Треугольник прямоугольный')
            else:
                print('Треугольник общего вида')
else:
    print('Треугольник построить нельзя')

