n = int(input())
a = [ int(x) for x in input().split() ]

ans = 0
q = 1

for i in range(n):
    if a[i] == q:
        q += 1
    else:
        ans += 1

if q == 1:
    print(-1)
else:
    print(ans)
