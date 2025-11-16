l = []
n,m = list(map(int,input().split()))
for i in range(n+1):
    l.append(i)
for _ in range(m):
    s,e = list(map(int,input().split()))
    while s<e:
        l[s],l[e] = l[e],l[s]
        s = s + 1
        e = e - 1

for i in range(1,n+1):
    print(l[i],end=" ")