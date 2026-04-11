import sys
sys.setrecursionlimit(10**6)




n = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
r1 = []
r2 = []
for i in range(n):
    a = list(input())
    r1.append(a[:])
    for j in range(n):
        if a[j] == 'R':
            a[j] = 'G'
    r2.append(a[:])
# print(*r1,sep="\n")
# print()
# print(*r2,sep="\n")

v = [[0] * n for _ in range(n)]
v2 = [[0] * n for _ in range(n)]
ans = 0
ans2 = 0

# 정상인용

def dfs(y,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0<= nx < n and v[ny][nx] == 0 and r1[ny][nx] == r1[y][x]:
            v[ny][nx] = 1 
            dfs(ny,nx)

 



for i in range(n):
    for j in range(n):
        if v[i][j] == 0 :
            v[i][j] = 1
            ans+=1
            dfs(i,j)




def dfs1(y,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0<= nx < n and v2[ny][nx] == 0 and r2[ny][nx] == r2[y][x]:
            v2[ny][nx] = 1 
            dfs1(ny,nx)


for i in range(n):
    for j in range(n):
        if v2[i][j] == 0 :
            v2[i][j] = 1
            ans2+=1
            dfs1(i,j)

print(ans,ans2)