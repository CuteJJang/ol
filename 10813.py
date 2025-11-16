n,m = list(map(int,input().split()))

l=[]

for i in range(n+1):
    l.append(i)
for p in range(m):
    s,e = list(map(int,input().split()))
    l[s],l[e] = l[e],l[s]
print(*l[1:])    