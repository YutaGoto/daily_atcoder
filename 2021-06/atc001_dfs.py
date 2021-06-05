import sys
h, w = map(int,input().split())

sys.setrecursionlimit((h+1)*(w+1))

maze = []

for i in range(h):
    maze.append(list(input()))


reached = [[False]*w for i in range(h)]


for i in range(h):
    for j in range(w):
        if maze[i][j] == "s":
            sx, sy = i, j

        if maze[i][j] == "g":
            gx, gy = i, j


def search(x,y):
    # xyの位置が壁か範囲外かどうか
    if x < 0 or h <= x or y < 0 or w <= y or maze[x][y] == "#":
        return
    # 探索済みかどうか
    if reached[x][y]:
        return

    reached[x][y] = True

    search(x+1, y)
    search(x-1, y)
    search(x, y+1)
    search(x, y-1)


search(sx,sy)

if reached[gx][gy]:
    print('Yes')
else:
    print('No')
