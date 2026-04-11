from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t= int(input())

def dfs(x,c):
    v [x] = c
    re = True
    for i in r[x]:
        if v[i] == -1:
            re = dfs(i,(c+1)%2)

        if v[i] == c:
            re =  False
        
        if re == False:
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

    re = dfs(1,1)

    for h in range(1,n+1):
        if v[h] == -1:
            if dfs(h,1) ==False:
                re = False
                break

    if re == False:
        print("NO")
    else:
        print("YES")    
    