from collections import deque


n = int(input())
m = int(input())

r = [[0] * (n+1) for _ in range(n+1)]
v = [0] * (n+1)
for i in range(m):
    a,b = map(int,input().split())
    r[a][b] = 1
    r[b][a] = 1

q = deque()
ans = 0
q.append(1)
v[1] = 1

while q:
    k = q.popleft()
    for i in range(1,n+1):
        if r[k][i] == 1 and v[i] == 0:
            v[i] = 1
            q.append(i)
            ans +=1
# print(sum(v)-1)
print(ans)
