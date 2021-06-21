n = int(input())
s = list(input())
ans = 3*10**5 + 1

wp = [0] * n
ep = [0] * n

for i in range(n):
    if s[i] == 'E':
        ep[i] = 1
    else:
        wp[i] = 1

for i in range(1, n):
    wp[i] += wp[i-1]
    ep[i] += ep[i-1]


for i in range(n):
    t = 0
    if i != 0:
        t += wp[i-1]
    t += ep[n-1] - ep[i]
    ans = min(ans, t)

print(ans)
