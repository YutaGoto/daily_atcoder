n = int(input())
s = 0.0

for i in range(n):
    x, u = input().split(' ')
    if u == 'JPY':
        s += float(x)
    else:
        s += float(x)*380000

print(s)
