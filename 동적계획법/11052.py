n = int(input())
l = [0] + list(map(int,input().split()))

dp = [0] * (n+1) 

for j in range(1,n+1):
    for i in range(1,n+1):

        if i - j >= 0:
            dp[i] = max(dp[i],dp[i-j]+l[j])
        else:
            dp[i] = dp[i]
print(dp[-1])



