n,m = map(int,input().split())

a,b = [] , []
c = []
for _ in range(n):
    l = list(map(int,input().split()))
    a.append(l)

for _ in range(n):
    l = list(map(int,input().split()))
    b.append(l) 
    
for _ in range(n):
    l = [0] * m
    c.append(l) 
    
for i in range(n):
    for j in range(m):
        c[i][j] = a [i][j] + b[i][j]

for i in range(n):
    for j in range(m):
        print(c[i][j],end=" ")
    print()
