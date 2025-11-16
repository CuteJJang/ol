t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    l = []
    for d in range(k+1):
        l.append([0]*(n+1))
        
    for c in range(n+1):
        l[0][c] = c
    for p in range(1,k+1):
        for b in range(1,n+1):
            l[p][b] = l[p][b-1] + l[p-1][b]
    print(l[k][n])