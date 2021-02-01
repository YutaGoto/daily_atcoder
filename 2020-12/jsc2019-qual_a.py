m, d = map(int, input().split())

c = 0

for j in range(1, m+1):
    for i in range(1, d+1):
        d10 = i // 10
        d1 = i % 10
        if d10 >= 2 and d1 >= 2 and d10 * d1 == j:
            c += 1

print(c)
