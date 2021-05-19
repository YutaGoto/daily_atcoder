s = list(input())
lens = len(s)
ans = 0
aflag = False

for i in range(lens):
    if aflag:
        c += 1
        if s[i] == 'Z':
            ans = max(ans, c)
    else:
        if s[i] == 'A':
            aflag =  True
            c = 1

print(ans)
