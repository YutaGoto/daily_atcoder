import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


n = int(input())

c = 0

for i in range(2, n):
    if is_prime(i):
        c += 1

print(c)
