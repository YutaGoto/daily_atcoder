n = int(input())
a = [ int(x) for x in input().split() ]
ans = [0] * n

for i in range(n-1):
    ans[a[i]] += 1

for i in range(1, n):
    print(ans[i])

print(0)