d, n = map(int, input().split())

if n == 100:
    n += 1

if d == 0:
    print(n)
else:
    print(100**d * n)
