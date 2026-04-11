from collections import deque


n = int(input()) 
m = int(input())

r = [[0]*(n+1) for _ in range(n+1)]
v = [0]*(n+1) 

q = deque()
for i in range(m):
    a,b = map(int,input().split())
    r[a][b] = 1
    r[b][a] = 1

q.append(1)
v[1] = 1
while q:
    k = q.popleft()
    l = r[k]
    for i in range(n+1):
        if l[i] == 1 and v[i] == 0:
            q.append(i)
            v[i] = v[k]+1

ans = 0            
for i in v:
    if i == 2 or i == 3:
        ans+=1
print(ans)