n, x = map(int, input().split())
l = []
c = n

for _ in range(n):
  l.append(int(input()))

x -= sum(l)

c += x //min(l)
print(c)
