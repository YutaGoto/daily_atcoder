n, a = map(int, input().split())
x = [ int(c) for c in input().split() ]

dp = [[[0] * 2501 for i in range(51)] for j in range(51)]
dp[0][0][0] = 1

for i in range(n):
    for j in range(n):
        for k in range(2500):
            if dp[i][j][k]:
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j+1][k + x[i]] += dp[i][j][k]

ans = 0
for i in range(1,n+1):
    ans += dp[n][i][i*a]

print(ans)
