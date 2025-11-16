# from collections import deque


# n = int(input())

# path = {}
# for i in range(1,n+1):
#     path[i] = []

# v = [0] * (n+1)


# m = int(input())

# for _ in range(1,m+1):
#     a,b = map(int,input().split())
#     path[a].append(b)
#     path[b].append(a)
    
# q = deque()
# v[1] = 1
# q.append(1)


# while q:
#     p = q.popleft()
    
#     for node in path[p]:
#         if v[node] == 1:
#             continue
#         q.append(node)
#         v[node ] = 1
        
        
# print(sum(v)-1)


n = int(input())
m = int(input())
path = [ [] for i in range(n+1)]
for i in range(m):
    a,b, = map(int,input().split())
    path[a].append(b)
    path[b].append(a)
    
v = [0] * (n+1)
    
def dfs(x):
    ans = 0
    for i in path[x]:
        if v[i] == 1:
            continue
        v[i] = 1
        ans += dfs(i) + 1
        
    return ans    
v[1] = 1

print(dfs(1))
