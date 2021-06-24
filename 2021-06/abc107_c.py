n, k = map(int,input().split())
l = [ int(x) for x in input().split() ]

ans = 10**9

for i in range(n-k+1):
    if k == 1:
        ans = min(ans, abs(l[i]))
    else:
        first = l[i]
        last = l[i+k-1]
        if first < 0 and last > 0:
            if abs(first) - abs(last) > 0:
                t = abs(last) * 2 + abs(first)
                ans = min(ans, t)
            else:
                t = abs(last) + abs(first) * 2
                ans = min(ans, t)
        else:
            t = max(abs(last), abs(first))
            ans = min(ans, t)


print(ans)
