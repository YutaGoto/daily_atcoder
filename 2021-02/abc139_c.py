n = int(input())
h = [ int(x) for x in input().split() ]

mx = 0
t = 0

for i in range(n):
    if i == n-1:
        mx = max(mx, t)
    elif h[i] >= h[i+1]:
        t += 1
    else:
        mx = max(mx, t)
        t = 0

print(mx)
