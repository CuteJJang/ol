n = int(input())

l = []
dp = []

for _ in range(n):
    l.append(list(map(int,input().split())))
    dp.append([0]*3)

dp[0][0] = l[0][0]
dp[0][1] = l[0][1]
dp[0][2] = l[0][2]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + l[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + l[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][0]) + l[i][2]

print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))