n = int(input())
ans = 1

for i in range(n):
    a = [ int(x) for x in input().split() ]
    ans *= sum(a)

print(ans % 1000000007)
