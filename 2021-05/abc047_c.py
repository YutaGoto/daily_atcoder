s = list(input())

slen = len(s)
cur = ""
newlist = []

for i in range(slen):
    if cur == "":
        cur = s[i]
        newlist.append(s[i])
    elif s[i-1] != s[i]:
        cur = s[i]
        newlist.append(s[i])

print(len(newlist) - 1)
