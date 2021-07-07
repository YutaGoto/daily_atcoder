n = int(input())

cl = []
sl = []
fl = []

for i in range(n-1):
    c, s, f = map(int,input().split())
    cl.append(c)
    sl.append(s)
    fl.append(f)

for i in range(n-1):
    ans = 0

    for j in range(i, n-1):
        ans = max(ans, sl[j])
        d = ans - sl[j]
        if d % fl[j] != 0:
            d = fl[j] - (d % fl[j])
        else:
            d = 0

        ans += d + cl[j]


    print(ans)

print(0)
