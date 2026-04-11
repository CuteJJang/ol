from collections import deque


n,k = map(int,input().split())

v = [0]* 100001

q = deque()
q.append(n)
v[n] = 1
while q:
    x = q.popleft()
    nx = x+1
    if 0<= nx < 100001 and v[nx] == 0:
        v[nx] = v[x]+1
        q.append(nx)
    nx = x-1
    if 0<= nx < 100001 and v[nx] == 0:
        v[nx] = v[x]+1
        q.append(nx)

    nx = x*2    
    if 0<= nx < 100001 and v[nx] == 0:
        v[nx] = v[x]+1
        q.append(nx)

    if v[k] !=0:
        print(v[k]-1)
        exit()


    
