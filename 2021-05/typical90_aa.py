n = int(input())
signed = set([])
plen = 0

for i in range(n):
    s = input()
    signed.add(s)
    if plen < len(signed):
        print(i+1)
        plen = len(signed)
