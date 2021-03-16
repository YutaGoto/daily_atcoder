n = int(input())
a = [ int(x) for x in input().split() ]

o = list(filter(lambda x: x % 2 == 0, a))
y = list(filter(lambda x: x % 4 == 0, o))

yon = len(y)
guusuu = len(o)
ni = guusuu - yon
kisuu = n - guusuu

if ni >= 1:
    kisuu += 1

if yon+1 >= kisuu:
    print("Yes")
else:
    print("No")
