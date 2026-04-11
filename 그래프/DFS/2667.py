n = int(input())
v = [[0] * n for _ in range(n)]
r = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(n):
    a = list(map(int,input()))
    r.append(a)

def dfs(y,x,a): 
    v[y][x] = a
    cnt = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < n and 0 <= nx < n and r[ny][nx] == 1 and v[ny][nx] == 0:
            v[ny][nx] = 1
            cnt += dfs(ny,nx,t)
    return cnt

t = 1
ans = []
for i in range(n):
    for j in range(n):
        if r[i][j] == 1 and v[i][j] == 0:
            v[i][j] = 1
            ans.append(dfs(i,j,t))
            t += 1 

print(len(ans))
ans.sort()
print(*ans,sep="\n")