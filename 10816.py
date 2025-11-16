from collections import defaultdict


n = int(input())
a = list(map(int,input().split()))
m = int(input())
l = list(map(int,input().split()))
d = defaultdict(int)
for i in a:
    d[i]+=1
for i in l:
    if d[i] == 1:
        print(d[i], end= ' ')
    else:
        print(d[i], end=' ')
        