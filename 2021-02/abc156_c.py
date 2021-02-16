from decimal import Decimal, ROUND_HALF_UP

n = int(input())
l = [ int(x) for x in input().split() ]

ave = Decimal(str(sum(l) / n)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

c = 0

for e in l:
    c += (e-ave)**2

print(c)
