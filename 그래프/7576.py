from collections import deque


m,n = map(int,input().split())
r = [list(map(int,input().split())) for _ in range(n)]

q = deque()

# print(*r,sep="\n")
for i in range(n):
    for j in range(m):
        if r[i][j] == 1:
            q.append((i,j))

dy = [-1,1,0,0]
dx = [0,0,1,-1]

ans = 1
while q:
    y,x = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= ny < n and 0 <= nx < m and r[ny][nx] == 0 :

            r[ny][nx] = r[y][x] + 1
            q.append((ny,nx))
            if r[ny][nx] > ans:
                ans = r[ny][nx]
for i in range(n):
    for j in range(m):
        if r[i][j] == 0:
            print(-1)
            exit()

# max = -2
# print(*r, sep="\n")
print(ans-1)
# for i in range(n):
#     for j in range(m):
#         if r[i][j] > max:
#             max = r[i][j]
        

