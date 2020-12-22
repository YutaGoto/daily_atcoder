n = int(input())

k = []

for _ in range(n):
    a = int(input())
    k.append(a)

k.sort()
ans = 0
ptr = 0

while ptr < n:
    r = 0
    c = k[ptr]
    while ptr < n and k[ptr] == c:
        r += 1
        ptr += 1

    ans += r%2

print(ans)
