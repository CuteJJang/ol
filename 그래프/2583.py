from collections import deque


m,n,k = map(int,input().split())
r = [[0] * n for _ in range(m)]
v = [[0] * n for _ in range(m)]
for _ in range(k):
    x,y,x2,y2 = map(int,input().split())
    for j in range(y,y2):
        for i in range(x,x2):
 
            r[j][i] = 1
ans = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def solve(y,x):

    q= deque()
    q.append((y,x))
    v[y][x] = 1
    cnt = 1
    while q:
        yy,xx = q.popleft()
        for i in range(4):
            new_x = xx + dx[i]
            new_y = yy + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m and r[new_y][new_x] == 0 and v[new_y][new_x] == 0:
                v[new_y][new_x] = 1
                cnt+=1
                q.append((new_y,new_x))

    return cnt






# print(*r,sep="\n")
for i in range(m):
    for j in range(n):
        if r[i][j] == 0 and v[i][j] == 0:
            t = solve(i,j)
            ans.append(t)
print(len(ans))
ans.sort()
print(*ans)

