n = int(input())

c = 1

for i in range(1, n+1):
    c *= i
    if c > 1000000007:
        c %= 1000000007

print(c)
