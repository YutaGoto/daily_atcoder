a = input()
b = input()
c = input()

d = {'a': 0, 'b': 0, 'c': 0}

t = 'a'

while True:
    d[t] += 1
    if d[t] > len(vars()[t]):
        print(t.upper())
        exit()
    t = vars()[t][d[t]-1] 
