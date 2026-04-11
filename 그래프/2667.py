from collections import deque


n = int(input())
r = [list(map(int,input())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
d = 1 
ans = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(n):
        if r[i][j] == 1 and v [i][j] == 0:
            q = deque()
            v [i][j] =d
            q.append((i,j))
            t = 1

            while q:
                y,x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= nx < n and 0<=ny <n and r[ny][nx] == 1 and v[ny][nx] == 0:
                       v[ny][nx] = d
                       q.append((ny,nx))
                       t+=1
            ans.append(t)
            d+=1
# print(*v,sep="\n")
# print()
print(d-1)
ans.sort()
print(*ans,sep="\n")


