n, m = map(int, input().split())

k = [0] * 32

for _ in range(n):
    l = [ int(x) for x in input().split() ]
    for i, e in enumerate(l):
        if i != 0:
            k[e] += 1

print(k.count(n))
