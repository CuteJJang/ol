n = int(input())
l = list(map(int,input().split()))
d = {}

for i in l:
    d[i] = 1
    
d = d.keys()
d = list(d)
d.sort()
for i in d:
    print(i,end=" ")