n = int(input())

l = [int(input())for _ in range(n)]
if n == 1:
    print(l[0])
elif n == 2:
    print(max(l[1]+l[0],l[1])) 
elif n == 3:
    print(max(l[0]+l[2],l[1]+l[2])) 
else:
    dp=[0] *n
    dp[0] = l[0]
    dp[1] = max(l[1]+l[0],l[1])
    dp[2] = max(l[0]+l[2],l[1]+l[2])
    for i in range(3,n):
        dp[i] = max(dp[i-2]+l[i],l[i-1]+l[i]+dp[i-1-2])
        
    print(dp[-1])