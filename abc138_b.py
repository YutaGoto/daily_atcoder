n = int(input())
a = [ int(x) for x in input().split() ]

bunbo = 0
for e in a:
    bunbo += 1/e

print(1/bunbo)
