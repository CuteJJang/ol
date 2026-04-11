from collections import deque


n = int(input())
r = [list(map(int,input().split())) for _ in range(n)]
ans = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def solve(h):
    q = deque()
    v = [[0] * n for _ in range(n)]
    aans = 0
    for i in range(n):
        for j in range(n):
            if r[i][j] > h and v[i][j] == 0:
                v[i][j] = 1
                aans+=1
                q.append((i,j))
                while q:
                    y,x = q.popleft()

                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0<= ny < n and 0<= nx < n and r[ny][nx] > h and v[ny][nx] == 0:
                            q.append((ny,nx))
                            v[ny][nx] = 1
    return aans


for i in range(1,100):
    ans = max(ans,solve(i))

print(ans)