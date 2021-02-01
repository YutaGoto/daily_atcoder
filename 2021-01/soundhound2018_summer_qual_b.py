s = input()
w = int(input())

c = 0
a = ''

for e in list(s):
    if c == 0:
        a += e

    c += 1

    if c == w:
        c -= w

print(a)
