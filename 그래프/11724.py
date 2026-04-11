from collections import defaultdict, deque


n,m = map(int,input().split())

r = defaultdict(list)
v = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    r[a].append(b)
    r[b] . append(a)

q = deque()
ans = 0
for i in range(1,n+1):
    if v[i] == 0:
        q.append(i)
        v[i] = 1
        ans+=1
        while q:
            k = q.popleft()
            for t in r[k]:
                if v[t] == 0:
                    q.append(t)
                    v[t] = 1


print(ans)