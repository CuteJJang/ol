from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

q = deque()

for i in range(n):
    x = list(map(int,input().split()))
    if x[0] == 1:
        q.appendleft(x[1])
    elif x[0] == 2:
        q.append(x[1])
    elif x[0] == 3:
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif x[0] == 4:
        if len(q) != 0:
            print(q.pop())
        else:
            print(-1)
    elif x[0] == 5:
        print(len(q))
    elif x[0] == 6:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 7:
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    else:
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)
                