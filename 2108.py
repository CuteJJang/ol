from collections import defaultdict


n = int(input())

l = [int(input())for i in range(n)]

k = sum(l)/n
ans = k//1
if k%1>=0.5:
    ans+=1
print(int(ans))

sl = sorted(l)
print(sl[n//2])

d = defaultdict(int)

mm = 0    
for i in l:
    d[i] +=1
    
    mm = max(d[i], mm)
    
l2 = []    
for k,v in d.items():
    if v == mm:
        l2.append((k,v))

l2.sort()   

if len(l2) == 1:
    print(l2[0][0])
else:
    print(l2[1][0])
print(max(l) - min(l))
