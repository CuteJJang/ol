from collections import deque
from itertools import combinations

n,m = map(int,input().split())
r = [list(map(int,input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0

walls = []
st = []
for i in range(n):
    for j in range(m):
        if r[i][j] == 0:
            walls.append( (i,j) )
        if r[i][j] == 2:
            st.append((i,j))


c = list(combinations(walls,3))



def solve(w):
    v = [[0] * m for _ in range(n)]
    q = deque()
    for i,j in st:
        q.append((i,j))
        v[i][j] = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny <n and 0<= nx < m and v[ny][nx] == 0 and r[ny][nx] == 0 and  not (ny,nx)in w:
                q.append((ny,nx))
                v[ny][nx] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if v[i][j] == 0 and r[i][j] == 0:
                count+=1
    return count-3

for w in c:
    ans = max(ans,solve(w))
print(ans)