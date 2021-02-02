n = int(input())
a = [ int(x) for x in input().split() ]
b = [ int(x) for x in input().split() ]

mon = 0

for i in range(n):
    if a[i] >= b[i]:
        mon += b[i]
    else:
        mon += a[i]
        b[i] -= a[i]

        if a[i+1] >= b[i]:
            mon += b[i]
            a[i+1] -= b[i]
        else:
            mon += a[i+1]
            a[i+1] = 0

print(mon)
