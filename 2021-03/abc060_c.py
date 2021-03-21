n, oyut = map(int, input().split())
t = [ int(x) for x in input().split() ]

c = 0

for i in range(n):
    if i == n-1:
        c += oyut
        break
    if t[i+1] - t[i] < oyut:
        c += t[i+1] - t[i]
    else:
        c += oyut

print(c)
