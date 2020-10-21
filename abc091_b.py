n = int(input())

d1 = {}
for _ in range(n):
  s = input()
  if s in d1:
    d1[s] += 1
  else:
    d1[s] = 1

m = int(input())

for _ in range(m):
  t = input()
  if t in d1:
    d1[t] -= 1

ma = max(d1.values())
if ma <= 0:
  print(0)
else:
  print(ma)
