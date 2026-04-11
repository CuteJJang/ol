from collections import deque


t = int(input())
dy = [1,-1,0,0]
dx = [0,0,1,-1]

def solve():
    m,n,k = map(int,input().split())
    # m 가로 n 세로 k  배추위치
    r = [[0] * m for _ in range(n)]
    v = [[0] * m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        r[y][x] = 1

    # print(*r ,sep="\n")
    ans = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if r[i][j] == 1 and v[i][j] == 0:
                q.append((i,j))
                v[i][j] = 1
                ans+=1
                # print(i,j)
                while q:
                    y,x = q.popleft()
                    for c in range(4):
                        ny = y + dy[c]
                        nx = x + dx[c]
                        if 0 <= ny < n and 0 <= nx <m and r[ny][nx] == 1 and v[ny][nx] == 0:
                           q.append((ny,nx))
                           v[ny][nx] = 1 
    
    print(ans)

 
 

for _ in range(t):
    solve()