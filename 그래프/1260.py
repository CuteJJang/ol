from collections import deque


n,m,v = map(int,input().split())

r = [[0] * (n+1) for _ in range(n+1)] 

for i in range (m):
    a,b = map(int,input().split())
    r[a][b] = 1
    r[b][a] = 1



vi = [0] * (n+1)
ans = []

def DFS(t):
    for i in range(1,n+1):
        if r[t][i] == 1 and vi[i] == 0:
            ans.append(i)
            vi[i] = 1
            DFS(i)

vi[v] = 1
ans.append(v)
DFS(v)
print(*ans)





q = deque ()
vi = [0] * (n+1)
ans = []

q.append(v)
vi[v] = 1
ans.append(v)

while q:
    t = q.popleft()
    for i in range(1,n+1):
        if r[t][i] == 1 and vi[i] == 0:
            q.append(i)
            vi[i] =1
            ans.append(i)

print(*ans)