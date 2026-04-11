n = int(input())
 
l = []
dp = []
for _ in range(n):
    l.append(list(map(int,input().split())))
    dp.append([0]*n)

dp[0][0] = l[0][0]

for i in range(n-1):
    for j in range(i+1):
        dp[i+1][j] = max(dp[i+1][j],dp[i][j]+l[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+l[i+1][j+1])

print(max(dp[n-1]))