d, g = map(int, input().split())

p = []
c = []
ans = 10000000000

for _ in range(d):
    tp, tc = map(int, input().split())
    p.append(tp)
    c.append(tc)

for i in range(1 << d):
    s = 0
    n = 0
    rmax = -1
    for j in range(d):
        if i >> j & 1:
            s += 100 * (j+1) * p[j] + c[j]
            n += p[j]
        else:
            rmax = j
    if s < g:
        s1 = 100 * (rmax+1)
        need = (g-s+s1-1)//s1
        if need >= p[rmax]:
            continue
        n += need
    ans = min(ans, n)

print(ans)
