l = [ int(x) for x in input().split() ]
ans = 0
l.sort()

if l[1] < l[2] - 1:
    sa = l[2] - l[1]
    ans += sa // 2
    l[1] += sa // 2 * 2


if l[0] < l[2] - 1:
    sa = l[2] - l[0]
    ans += sa // 2
    l[0] += sa // 2 * 2


l.sort()

if l[0] == l[1] != l[2]:
    ans += 1
    l[0] += 1
    l[1] += 1
elif l[0] != l[1] == l[2]:
    ans += 2
    l[0] += 2
    l[1] += 1
    l[2] += 1


print(ans)
