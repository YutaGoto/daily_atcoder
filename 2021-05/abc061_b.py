n, m = map(int, input().split())
ans = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    ans[a] += 1
    ans[b] += 1

for j in range(n+1):
    if j != 0:
        print(ans[j])
