n = int(input())
l = [ int(x) for x in input().split() ]
l.sort(reverse=True)

i = 0
k = [0,0]
j = 0

while i < n: 
    if i+1 != n and l[i] == l[i+1]: 
        k[j] = l[i]
        j += 1
        i += 1
    i += 1
    if j == 2:
        break

print(k[0] * k[1])
