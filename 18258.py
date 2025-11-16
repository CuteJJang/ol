from collections import deque
import sys
input = sys.stdin.readline

q = deque()

n = int(input())
for _ in range(n):
    s = input().split()
    if s[0] == "push":
        q.append(s[1])
    elif s[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif s[0] == "size":
        print(len(q))
    elif s[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif s[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
        
            