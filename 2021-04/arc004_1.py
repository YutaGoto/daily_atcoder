import itertools
import math

n = int(input())

pts = []

for _ in range(n):
    x, y = map(int, input().split())
    pts.append([x, y])

dmax = 0

for v in itertools.combinations(pts, 2):
    d = (v[0][0]-v[1][0])**2 + (v[0][1]-v[1][1])**2
    dmax = max(dmax, d)

print(math.sqrt(dmax))
