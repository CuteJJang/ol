from collections import deque


n,m = map(int,input().split())

r = [list(map(int,input()))for _ in range(n)]

v = [[0] * m for _ in range(n)]

q = deque()
q.append(((0),(0)))
v[0][0] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

while q:
    y,x = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0<= ny <n and r[ny][nx] == 1 and v[ny][nx] == 0:
            q.append((ny,nx))
            v[ny][nx] = v[y][x]+1

print(v[n-1][m-1])