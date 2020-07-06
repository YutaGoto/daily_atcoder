n = int(input())
x = [ int(x) for x in input().split() ]

s = sum(x)
avg = s // n

t = u = 0
for e in x:
    t += (e - avg)**2
    u += (e - (avg + 1))**2

print(min([t, u]))

