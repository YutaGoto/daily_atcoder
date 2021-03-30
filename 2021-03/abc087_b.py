a = int(input())
b = int(input())
c = int(input())
x = int(input())

q = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            cost = 500*i + 100*j + 50*k
            if cost == x:
                q += 1

print(q)
