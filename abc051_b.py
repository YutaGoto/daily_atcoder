k, s = map(int, input().split())
a = 0

for x in range(0, k+1):
    for y in range(0, k+1):
        z = s - x - y
        if z >= 0 and z <= k:
            a += 1

print(a)
