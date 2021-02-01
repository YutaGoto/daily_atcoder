n = int(input())
l = [ int(x) for x in input().split() ]

if 0 in l:
  print(0)
  exit()

t = 1
for e in l:
  t *= e
  if t > 1000000000000000000:
    print(-1)
    exit()

print(t)
