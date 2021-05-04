n, m = map(int, input().split())

q = [10] * n

for i in range(m):
    s, c = map(int, input().split())
    if q[s-1] == 10:
        q[s-1] = c
    elif q[s-1] == c:
        continue
    else:
        print(-1)
        exit()

ans = ""

for i in range(n):
    if n != 1 and i == 0:
        if q[i] == 0:
            print(-1)
            exit()
        elif q[i] == 10:
            ans += "1"
        else:
            ans += str(q[i])
    else:
        if q[i] == 10:
            ans += "0"
        else:
            ans += str(q[i])

print(ans)
