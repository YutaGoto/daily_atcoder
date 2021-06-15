import numpy as np

def eightto10(n):
    nums = list(str(n))
    nums.reverse()
    num = 0
    for i in range(len(nums)):
        num += int(nums[i]) * (8**i)

    return num

def eight_to_five(n):
    q = list(str(n))
    for i in range(len(q)):
        if q[i] == '8':
            q[i] = '5'

    return int(''.join(q))


n, k = map(int, input().split())
t = n

for _i in range(k):
    t = eightto10(t)
    t = np.base_repr(t, base=9)
    t = eight_to_five(t)


print(t)
