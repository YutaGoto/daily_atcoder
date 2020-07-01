import sys

a, b, x = map(int, input().split())

low = 0
high = 1000000000
k = a * high + b * len(str(high))
if k < x:
    print(high)
    sys.exit()

ans = [0]
while low <= high:
    mid = (low + high) // 2
    k = a * mid + b * len(str(mid))

    if k == x:
        print(mid)
        sys.exit()
    elif k > x:
        high = mid - 1
    else:
        ans.append(mid)
        low = mid + 1

print(max(ans))
