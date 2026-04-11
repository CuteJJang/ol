from collections import defaultdict


n = int(input())
for i in range(n):
    l = list(map(int,input().split()))
    l2 = {}
    s = -1
    for j in l[1:]:
        if j not in l2:
            l2[j]=0
        
        l2[j]+=1 
        if l[0]//2+1 <= l2[j]:
            s = j

    if s != -1:
        print(s)
    else:
        print('SYJKGW')

