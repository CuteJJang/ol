from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

n= int(input())

r = defaultdict(list)

for i in range(n-1):
    a,b,w = map(int,input().split())
    r[a].append((b,w))
    r[b].append((a,w))

v = [-1] * (n+1) 
v[1]                =                  0

def DFS(k):
    ans = k
    for c,w in r[k]:
        if v[c] == -1 :
            v[c]       =    v[k]         +           w
            t = DFS(c)

            if v[ans] < v[t]:
                ans = t
    return ans


st =DFS(1)
v = [-1] * (n+1)
v[st] = 0 
en = DFS(st)
print(v[en])