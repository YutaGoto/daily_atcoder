n = int(input())
a = [ int(x) for x in input().split() ]
a.sort(reverse=True)
ans = 0

for i in range(2*n):
    if i % 2 == 1:
        ans += a[i]

print(ans)
