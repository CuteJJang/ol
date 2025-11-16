t = int(input())

def solve(n):
        
    ans = [0] * (n+4)
    ans[0] = 1 
    ans[1] = 1
    ans[2]  = ans[1] + ans[0]
    ans[3]  = ans[2] + ans[1] + ans[0] 
    for i in range(4,n+1):
        ans[i] = ans[i-1] + ans[i-2] + ans[i-3]
       
    print(ans[n])
    
dp = [0] * 12        
def solve2(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    if dp[n] != 0:
        return dp[n]
    
    ans = 0
    ans = solve2(n-1) + solve2(n-2) + solve2(n-3)
    dp[n] = ans
    return ans 
    
for _ in range(t):
    n = int(input())
    # solve(n)
    print(solve2(n))