# s = int(input())
# n = 106 s минимальное???
for s in range(8, 1000):
    s = s // 7
    n = 1
    while s < 255:
        if (s + n) % 2 == 0:
            s = s + 11
            n = n + 5
    print(n)
