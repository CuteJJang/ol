t = int(input())
def solve():
    n = int(input())
    l = [[0] + list(map(int,input().split())) for _ in range(2)]
    dp = [[0] * (n+1) for _ in range(3)]
    dp[0][1] = l[0][1]
    dp[1][1] = l[1][1]
    
    for i in range(2,n+1):
        dp[0][i] = l[0][i] + max(dp[1][i-1],dp[1][i-2])
        dp[1][i] = l[1][i] + max(dp[0][i-1],dp[0][i-2])
    # print(*dp, sep="\n")
    print(max(dp[1][-1],dp[0][-1]))

for i in range(t):
    solve()