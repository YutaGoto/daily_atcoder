n, k = map(int, input().split())

l = [0] * 100001

for _ in range(n):
    a, b = map(int, input().split())
    l[a] += b

for i in range(100001):
    if k <= l[i]:
        print(i)
        exit()
    k -= l[i]
