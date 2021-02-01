n = int(input())

pl = []

for _ in range(n):
    a, b = map(int, input().split())
    pl.append([a, b])

pl.sort()

cn = 0
cp = 10000000000

for e in pl:
    if e[0] - cn > cp - e[1]:
        cn += cp - e[1]
        cp = e[1]
    else:
        cn += e[0] - cn
        cp = e[1]

cn += cp

print(cn)
