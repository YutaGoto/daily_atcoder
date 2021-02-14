h, w = map(int, input().split())

rownames = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
columnnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'W', 'X', 'Y', 'Z']

for i in range(h):
    l = input().split()
    if 'snuke' in l:
        row = rownames[i]
        column = columnnames[(l.index('snuke'))]
        print(column + row)
        exit()
