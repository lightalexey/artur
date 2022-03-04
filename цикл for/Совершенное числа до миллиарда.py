for a in range(6,1000000000):
    summa=0
    for i in range(1,a):
        if a%i==0:
            summa=summa+i
    if a==summa:
        print(a)

