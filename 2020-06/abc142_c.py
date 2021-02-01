n = int(input())
a = [ int(x) for x in input().split() ]
b = []

for i in range(n):
    b.append(a.index(i + 1) + 1)

c = map(str, b)
print(' '.join(c))
