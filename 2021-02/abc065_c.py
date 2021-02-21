import math

n, m = map(int, input().split())
qqq = 1000000007

np = math.factorial(n)
mp = math.factorial(m)

if abs(m - n) >= 2:
    print(0)
elif abs(m - n) == 1:
    print((np * mp) % qqq)
else:
    print(2*(np * mp) % qqq)
