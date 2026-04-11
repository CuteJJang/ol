from collections import deque


n = int(input())
l = list(map(int,input().split()))
q = deque()
t = []
for  i  in range(n-1,-1,-1):
    c=l[i]
    for j in range(c):
        t.append(q.popleft())

    q.appendleft(i+1)

    while t:
        q.appendleft(t.pop())

print(*list(q))