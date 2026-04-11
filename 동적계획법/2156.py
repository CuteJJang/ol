n = int(input())
dp = [[0] * (n + 1) for _ in range(3)]

l = [0]

for _ in range(n):
    l.append(int(input()))

ans = l[1]
dp[1][1] = l[1]
for i in range(2,n+1):
    dp[0][i] = max(dp[0][i-1],dp[2][i-1],dp[1][i-1])
    dp[1][i] = max(dp[1][i-2],dp[2][i-2],dp[0][i-1]) + l[i]
    dp[2][i] = dp[1][i-1] + l[i]
    ans = max(ans,dp[0][i],dp[1][i],dp[2][i])

print(ans)