import sys

def input():
    return sys.stdin.readline().rstrip()


n,m = map(int,input().split())
d = {}
for i in range(1,n+1):
    s = input()
    d[str(i)] = s
    d[s] = i
for i in range(m):
    e = input()
    print(d[e])
    