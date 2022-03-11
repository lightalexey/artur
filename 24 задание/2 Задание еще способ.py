# Определите длину самой длинной последовательности, состоящей из символов X.
# Хотя бы один символ X находится в последовательности.

# f = open('24_demo.txt')
# s = f.read()
# result = 1
# tek = 1
# s = s.replace('Y', ' ')
# s = s.replace('Z', ' ')
# a = s.split()
# print(a)
# print(len(max(a)))

print(len(max(open('24_demo.txt').read().replace('Y', ' ').replace('Z', ' ').split())))