# s = input('Введи строку:')
s = 'Мама мыла раму!'
k = len(s)
print('Количество символов:', k)
print('Первый символ:', s[0])
print('1 способ. Последний символ:', s[k-1])
print('2 способ. Последний символ:', s[-1])
print('Первое слово:', s[0:4])
k_a = 0
for i in range(k):
    if s[i] == 'а':
        k_a += 1
print('1 способ. Количество букв а:', k_a)
print('2 способ. Количество букв а:', s.count('а'))
# s[0] = 'м' СТРОКУ ИЗМЕНИТЬ НЕЛЬЗЯ!!!
s = s.replace('Мама', 'папа')
print(s)
s = s.replace('п', 'П', 1)
print(s)
if 'Папа' in s:
    print('Слово папа есть в предожении')
else:
    print('Слово папа отсутствует.')