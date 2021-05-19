import queue

k = int(input())
q = queue.Queue()

for i in range(1,10):
    q.put(i)

for j in range(k):
    c = q.get()

    if c % 10 != 0:
        q.put(10*c + c % 10 - 1)

    q.put(10*c + c % 10)

    if c % 10 != 9:
        q.put(10*c + c % 10 + 1)

print(c)
