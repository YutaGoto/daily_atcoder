s = list(input())

lens = len(s)
ans = 0
a = [0]*(lens+1)

for i in range(lens):
    if s[i] == '<':
        a[i+1] = a[i]+1

for j in range(lens-1, -1, -1):
    if s[j] == '>':
        a[j] = max(a[j+1]+1, a[j])

print(sum(a))
