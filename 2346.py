from collections import deque


n = int(input())
l = list(map(int,input().split()))
l = list(zip(range(1,n+1),l))

q = deque()
for i in l:
    q.append(i)
    
while q:
    b,j = q.popleft()
    print(b)
    if len(q) == 0:
        break
    if j > 0:
        for _ in range(j-1):
            d = q.popleft()
            q.append(d)
    else:
        for _ in range(abs(j)):
            d = q.pop()
            q.appendleft(d)
            