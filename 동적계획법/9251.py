a = '0' +input()
b = '1' + input()
al = len(a)-1
bl = len(b)-1
dp = [[0] * (al+1) for _ in range(bl+1)]

for i in range(1,bl+1):
    for j in range(1,al+1):
        if b[i] == a[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[bl][al])
