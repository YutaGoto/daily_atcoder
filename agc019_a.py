q, h, s, d = map(int, input().split())
n = int(input())

q = q * 4
h = h * 2

if n % 2 == 0:
    print((n // 2) * min([2*q,2*h,2*s,d]))
else:
    print((n // 2) * min([2*q,2*h,2*s,d]) + min([q,h,s]))
