s = list(input())
ans = ''

for e in s:
    if e in ['O', 'D']:
        ans += '0'
    elif 'I' == e:
        ans += '1'
    elif 'Z' == e:
        ans += '2'
    elif 'S' == e:
        ans += '5'
    elif 'B' == e:
        ans += '8'
    else:
        ans += e

print(ans)
