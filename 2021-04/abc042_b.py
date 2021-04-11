n, l = map(int, input().split())

arr = []

for i in range(n):
    s = input()
    arr.append(s)

arr.sort()

print(''.join(arr))
