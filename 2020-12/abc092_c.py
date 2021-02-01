n = int(input())
a = [ int(x) for x in input().split() ]

k = [0] + a + [0]
q = []
t = 0

for i in range(len(k)-1):
    t += abs(k[i] - k[i+1])
    if i >= 1 and i < len(k)-1:
        if (min(k[i-1:i+2]) == k[i] or max(k[i-1:i+2]) == k[i]):
            q.append(min([abs(k[i-1] - k[i])*2, abs(k[i] - k[i+1])*2]))
        else:
            q.append(0)

for i, e in enumerate(a):
    print(t - q[i])
