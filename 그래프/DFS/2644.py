from collections import defaultdict


n = int(input())
s,e= map(int,input().split())

m = int(input())
v = [-1] * (n+1)
r = defaultdict(list)

for i in range(m):
    a,b  = map(int,input().split())
    r[a].append(b)
    r[b].append(a)

# print(*r.items(),sep="\n")

def dfs(k):
    if k == e:
        return 0 
    v[k] = 1
    # cnt = 0
    for i in r[k]:
        if v[i] == -1:
            # cnt = dfs(i)+1
            re = dfs(i)
            if re != -1:
                return re+1

           
    return -1       

 
print(dfs(s))
