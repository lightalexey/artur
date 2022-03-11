# Определите длину самой длинной последовательности, состоящей из символов X.
# Хотя бы один символ X находится в последовательности.

f = open('24_demo.txt')
s = f.read()
result = 1
tek = 1

for i in range(len(s)-1):
    if s[i] == s[i+1] == 'X':
        tek += 1
    else:
        if tek > result:
            result = tek
        tek = 1
print(max(tek, result))