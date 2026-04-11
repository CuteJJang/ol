


n,k = map(int,input().split())
l = []
dp = []
for _ in range(n):
    a,b = map(int,input().split())
    l.append((a,b))
    dp.append([0]*(k+1))

a,b = l[0]
for i in range(a,k+1):
    if i >= a:
        dp[0][i] = b
    dp[0][i] = b

for i in range(1,n):
    a,b = l[i]


    for j in range(k+1):
        if j-a < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],b + dp[i-1][j-a])
print(dp[-1][-1])