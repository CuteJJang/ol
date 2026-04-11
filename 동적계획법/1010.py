t = int(input())
def solve():
    n,m = map(int,input().split())
    dp = []
    for i in range(m+1):
        dp.append([0]*(m+1))
        dp[i][1] = i
        dp[i][i] = 1
    for j in range(2,m+1):
        for i in range(2,n+1):
            dp[j][i] = dp[j-1][i-1] + dp[j-1][i]
    print(dp[m][n])
    

    



for _ in range(t):
    solve() 