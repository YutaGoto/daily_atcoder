import collections

n = int(input())
v = [ int(x) for x in input().split() ]
k = 0

c1 = collections.Counter(v[0::2])
c2 = collections.Counter(v[1::2])

m1 = c1.most_common()
m2 = c2.most_common()

m1.append((0,0))
m2.append((0,0))

if m1[0][0] != m2[0][0]:
    print(n-(m1[0][1]+m2[0][1]))
else:
    print(min(n-(m1[1][1]+m2[0][1]), n-(m1[0][1]+m2[1][1])))

