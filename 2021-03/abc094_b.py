n, m, x = map(int, input().split())
a = [ int(x) for x in input().split() ]

cmin = 0
cmax = 0

for i in range(m):
    if a[i] < x:
        cmin += 1
    elif a[i] > x:
        cmax += 1

print(min(cmin, cmax))
