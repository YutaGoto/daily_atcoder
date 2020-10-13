n, k = map(int, input().split())
l = [ int(x) for x in input().split() ]

c = (n-1) // (k-1)
if c * (k-1) != n-1:
  c += 1

print(c)
