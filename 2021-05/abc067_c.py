n = int(input())
a = [ int(c) for c in input().split() ]

x = sum(a[0:n-1])
y = a[n-1]
ans = abs(x-y)

for i in range(2, n-1):
    x -= a[n-i]
    y += a[n-i]
    ans = min(ans, abs(x-y))

print(ans)
