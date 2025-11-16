n,m = map(int,input().split())
l = list(map(int,input().split()))

ans = 1e19

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            t = l[i]+l[j]+l[k]
            if t <= m and (ans < t or m < ans):
                ans = t
            elif t >m and t < ans:
                ans = t
print(ans)
                