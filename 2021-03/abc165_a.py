k = int(input())
a, b = map(int, input().split())

i = a // k

if i == 0:
    if a % k == 0 or b % k == 0:
        print('OK')
    else:
        print('NG')
    exit()

while k*i <= b:
    if a <= k*i <= b:
        print('OK')
        exit()
    i += 1

print('NG')
