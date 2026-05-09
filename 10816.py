


from collections import defaultdict


n = int(input())
l = list(map(int,input().split()))
m = int(input()) 
l2 = list(map(int,input().split()))
d = defaultdict(int)

for i in l:
    d[i]+=1

for i in l2:
    if d[i] >= 1:
        print(d[i],end=" ")

    else:
        print(0,end=" ")

