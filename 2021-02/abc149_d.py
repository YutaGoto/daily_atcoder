n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

c = 0
h = []

for i in range(n):
    if t[i] == 'r':
        if i < k or h[i-k] != 'p':
            c += p
            h.append('p')
        else:
            h.append('q')
    elif t[i] == 's':
        if i < k or h[i-k] != 'r':
            c += r
            h.append('r')
        else:
            h.append('q')
    elif t[i] == 'p':
        if i < k or h[i-k] != 's':
            c += s
            h.append('s')
        else:
            h.append('q')

print(c)
