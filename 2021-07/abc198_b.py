n = list(input())
lenn = len(n)

for i in range(lenn):
    revn = list(reversed(n))
    if revn == n:
        print('Yes')
        exit()

    n = ['0'] + n

print('No')
