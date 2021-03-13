n = int(input())
v = [ int(x) for x in input().split() ]
c = [ int(x) for x in input().split() ]

q = []

for i in range(n):
    q.append(v[i]-c[i])

print(sum(list(filter(lambda x: x > 0, q))))
