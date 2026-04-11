import sys
sys.setrecursionlimit(10**9)




n,m = map(int,input().split())

r = [list(map(int,input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def DFS(y,x):
    v[y][x] = 1
    ans = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and v[ny][nx] == 0 and r[ny][nx] == 1:
            ans += DFS(ny,nx)

    return ans

ans = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if r[i][j] == 1 and v[i][j] == 0:
            cnt+=1
            ans = max(ans,DFS(i,j))

print(cnt)
print(ans)