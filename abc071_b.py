import sys

s = sorted(input())
for c in list('abcdefghijklmnopqrstuvwxyz'):
    if not c in s:
        print(c)
        sys.exit()

print('None')
