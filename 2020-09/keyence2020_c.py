n, k, s = map(int, input().split())

l = []

for _ in range(k):
    l.append(str(s))

for _ in range(n-k):
    if s == 10**9:
        l.append('1')
    else:
        l.append(str(s+1))

print(' '.join(l))
