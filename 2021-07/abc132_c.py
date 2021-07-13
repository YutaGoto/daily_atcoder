n = int(input())
d = [ int(x) for x in input().split() ]
d.sort()

div = d[n//2] - d[n//2 - 1]
if div < 0:
    print(0)
else:
    print(div)
