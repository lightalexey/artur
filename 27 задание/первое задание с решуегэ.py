f = open('27-A_demo.txt')
n = int(f.readline())
summa = 0
delta = 10 ** 6
for i in range(n):
    a1, a2 = f.readline().split()
    # a1 = int(a1)
    # a2 = int(a2)
    a1, a2 = int(a1), int(a2)
    summa += max(a1, a2)
    if abs(a1 - a2) < delta and abs(a1 - a2) % 3 != 0:
        delta = abs(a1 - a2)

# print(summa, summa % 3)
print(summa - delta)

