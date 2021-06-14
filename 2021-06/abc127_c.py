n, m = map(int, input().split())

g = [0] * (n+2)

for i in range(m):
    l, r = map(int, input().split())
    g[l] += 1
    g[r+1] -= 1

ans = 0

for i in range(n+1):
    g[i+1] += g[i]
    if g[i] == m:
        ans += 1

print(ans)
