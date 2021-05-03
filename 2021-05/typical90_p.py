n = int(input())
a, b, c = map(int, input().split())

coin = 9999

for i in range(10000):
    for j in range(10000-i):
        cc = n - (a*i + b*j)
        if cc % c == 0 and cc >= 0:
            coin = min(coin, i+j+(cc//c))

print(coin)
