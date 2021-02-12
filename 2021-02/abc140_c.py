n = int(input())
b = [ int(x) for x in input().split() ]
a = [b[0]]

for i in range(n-1):
    if i == n-2:
        a.append(b[i])
    else:
        a.append(min(b[i], b[i+1]))

print(sum(a))
