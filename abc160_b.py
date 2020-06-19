x = int(input())
u = 0

u = (x // 500) * 1000
y = (x % 500)
u = u + (y // 5) * 5

print(u)
