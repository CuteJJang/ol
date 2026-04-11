n = int(input())
m = int(input())

r = [[0] * (n+1) for _ in range(n+1)]
v = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())

    r[a][b] = 1
    r[b][a] = 1



def dfs(x):
    for i in range(1,n+1):
        if r[x][i] == 1 and  not v[i]:
            v[i] = 1
            dfs(i)

v[1]= 1
dfs(1) 
ans = 0
for i in v:
    if i == 1:
        ans+=1
print(ans-1)