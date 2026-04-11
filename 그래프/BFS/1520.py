import sys
sys.setrecursionlimit(10**9)



n,m = map(int,input().split())

r =[list(map(int,input().split()))for _ in range(n)]
v = [[-1] * m for _ in range(n)]



dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(y,x):
    if y == n-1 and x == m-1:
        return 1

    if v[y][x] != -1:
        return v[y][x]
    

    ans = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and r[y][x] > r[ny][nx] :
            ans += DFS(ny,nx)
    v[y][x] = ans
    return ans

print(DFS(0,0))
