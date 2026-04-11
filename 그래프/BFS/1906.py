from collections import deque


n,m = map(int,input().split())
r = [list(map(int,input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]
cnt = 0
ans = 0
def BFS(y,x):
    v[y][x] = 1
    q = deque()
    q.append((y,x))
    ans = 1

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx <m and r[ny][nx] == 1 and v[ny][nx] == 0:
                q.append((ny,nx))
                v[ny][nx] = 1
                ans+=1
    return ans

for i in range(n):
    for j in range(m):
        if r[i][j] == 1 and v[i][j] == 0:
            cnt+=1
            ans = max(ans,BFS(i,j))

print(cnt)
print(ans)
