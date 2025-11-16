from collections import deque


t = int(input())
def solve():
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    
    sl = sorted(l)
    
    q = deque()
        
    for i in range(n):
        if i == m:
            q.append( (l[i],1))
        else:
            
            q.append((l[i],0))
    cnt = 0        
    while q:
        v,f = q.popleft()
        if sl[-1] == v:
            cnt+=1
            sl.pop()
            if f == 1:
                break
        else:
            q.append((v,f))
    print(cnt)
    
    
for i in range(t):
    
    solve()
    