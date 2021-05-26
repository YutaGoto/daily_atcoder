x,y,a,b = map(int, input().split())
ex = 0

while x*a <= x+b and x*a < y:
    x *= a
    ex += 1

bb = ((y-x) // b)
while x + b * bb >= y:
    bb -= 1

ex += bb
print(ex)
