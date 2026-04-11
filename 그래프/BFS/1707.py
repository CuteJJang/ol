from collections import defaultdict, deque
import sys
input = sys.stdin.readline
t= int(input())

def solve(x):
    q = deque()
    q.append(x)
    v[x] = 1

    while q:
        x = q.popleft()
        for i in r[x]:
            if v[i] == -1:
                v[i] = (v[x]+1)%2
                q.append(i)
            elif v[i] == v[x]:
                return False
    return True

    


for _ in range(t):
    n,m = map(int,input().split())
    r = defaultdict(list)
    for  _ in range(m):
        a,b = map(int,input().split())
        r[a].append(b)
        r[b].append(a)
    v = [-1] * (n+1)    

    re = True

    for h in range(1,n+1):
        if v[h] == -1:
            if solve(h) ==False:
                re = False
                break

    if re == False:
        print("NO")
    else:
        print("YES")    
    