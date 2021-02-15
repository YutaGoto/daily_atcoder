import math

a, b, n = map(int, input().split())

x = min(n, b-1)
f = math.floor(a*x / b) - a * math.floor(x/b)
print(f)
