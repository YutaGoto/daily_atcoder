def gcd(m, n):
    if m < n:
        m, n = n, m

    while True:
        r = m % n
        if r == 0:
            return n
        else:
            m, n = n, r

def lcm(a, b):
    return a*b // gcd(a, b)

a, b = map(int, input().split())
lcmn = lcm(a, b)
if lcmn > 1000000000000000000:
    print("Large")
else:
    print(lcmn)
