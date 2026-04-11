from collections import defaultdict, deque

q = deque()
n = int(input())
r = defaultdict(list)
v = [0] * (n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    r[a].append(b)
    r[b].append(a)



q.append(1)
v[1] = 1
while q:
    k = q.popleft()
    for t in r[k]:
        if v[t] == 0:
            v[t] = k
            q.append(t)
print(*v[2:],sep="\n")