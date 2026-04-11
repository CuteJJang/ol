from collections import deque


t = int(input())

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

def solve():
    n = int(input())
    y1,x1 = map(int,input().split())
    y2,x2 = map(int,input().split())
    v = [[0] * n for _ in range(n)]
    q = deque()
    q.append((y1,x1,0))
    v[y1][x1] = 1 
    while q:
        y,x,t = q.popleft()
        # v[y][x] = 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < n and v[ny][nx] == 0:
                v[ny][nx] = 1
                q.append((ny,nx,t+1))
                if ny == y2 and nx == x2:
                    return (t+1)
    return 0


for i in range(t):
    a = solve()
    print(a)
