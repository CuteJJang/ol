n,k  = map(int,input().split())

l = [0] + [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] =1


for j in range(1,n+1):
    for a in range(1,k+1) :
        if a - l[j]>=0:
            dp[a] = dp[a] + dp[a-l[j]]

print(dp[-1])


