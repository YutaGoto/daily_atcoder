n, k = map(int, input().split())
a = [ int(x) for x in input().split() ]

su = sum(a[0:k])
print(su)

for i in range(n-k):
    su = su - a[i] + a[i+k]
    print(su)
