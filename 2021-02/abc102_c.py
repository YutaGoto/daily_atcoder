from statistics import median

n = int(input())
a = [ int(x) for x in input().split() ]
na = []

for i, e in enumerate(a):
    na.append(e-(i+1))

b = median(na)
aa = []

for e in na:
    aa.append(abs(e - b))

print(int(sum(aa)))
