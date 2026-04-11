import sys

sys.setrecursionlimit(10**6)


dy = [0,0,1,-1,-1,1,1,-1]

dx = [1,-1,0,0,-1,-1,1,1]

def dfs(y,x):
    v[y][x] =1 
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < h and 0 <= nx < w and r[ny][nx] == 1 and v[ny][nx] == 0:
            dfs(ny,nx)



def solve():

    ans = 0

    for i in range(h):
        for j in range(w):
            if r[i][j] == 1 and v[i][j] == 0:
                dfs(i,j)
                ans+=1
    print(ans)

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    r = [list(map(int,input().split())) for _ in range(h)]

    v = [[0]*w for _ in range(h)]
    solve()