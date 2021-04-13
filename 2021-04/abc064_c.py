# レート 1-399：灰色
# レート 400-799：茶色
# レート 800-1199：緑色
# レート 1200-1599：水色
# レート 1600-1999：青色
# レート 2000-2399：黄色
# レート 2400-2799：橙色
# レート 2800-3199：赤色

n = int(input())
a = [ int(x) for x in input().split() ]

k = set()
any_count = 0

for e in a:
    if e < 400:
        k.add('gray')
    elif e < 800:
        k.add('brown')
    elif e < 1200:
        k.add('green')
    elif e < 1600:
        k.add('water')
    elif e < 2000:
        k.add('blue')
    elif e < 2400:
        k.add('yellow')
    elif e < 2800:
        k.add('orange')
    elif e < 3200:
        k.add('red')
    else:
        any_count += 1

if any_count == 0:
    print(len(k), len(k))
else:
    mn = max(len(k), 1)
    mx = len(k) + any_count

    print(mn, mx)
