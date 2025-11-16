import sys


sys.setrecursionlimit(10**7)

n = int(input())
dp = [1e10] * 1000001 *3

def solve2(n):
    dp[1] = 0
    for i in range(1,n+1):
        
        dp[i+1] = min(dp[i+1], dp[i] +1)
        dp[i*2] = min(dp[i*2],dp[i] +1)
        dp[i*3] = min(dp[i*3],dp[i] +1)
    return dp[n] 

print(solve2(n))

def solve(n): 
    if n == 1:
        return 0 
    
    if dp[n]!= 1e10:
        return(dp[n])
    
    ans = 9e1000000
    
    if n % 3 == 0:
        ans = min(ans, solve(n//3)+1)
    
    if n%2 == 0:
        ans = min(ans, solve(n//2)+1)
        
    
    ans = min(ans, solve(n-1)+1)
    
    dp[n] = ans
    
    return ans
