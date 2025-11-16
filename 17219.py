import sys


def input():
    return sys.stdin.readline().rstrip()



n,m = map(int,input().split())

d = dict()

for i in range(n):
    s = input().split()
    d[s[0]] = s[1]

for i in range(m):
    a = input()
    print(d[a]) 