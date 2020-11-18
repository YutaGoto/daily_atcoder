n, q = map(int, input().split())

t = [0] * (n+1)

for _ in range(q):
    l, r = map(int, input().split())
    t[l-1] += 1
    t[r] -= 1

ans = ''

for i in range(n):
    t[i+1] += t[i]
    if t[i] % 2 == 0:
        ans += '0'
    else:
        ans += '1'

print(ans)
