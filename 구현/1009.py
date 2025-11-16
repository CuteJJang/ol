def solve():
    a,b = map(int,input().split())
    ans = [a%10]
    
    for _ in range(1,b):
        n = ans[-1] * a % 10
        
        if ans[0] == n:
            break
        
        ans.append(n)
        
    l = len(ans)
    idx = (b-1)%l 
    if ans[idx] == 0:
        print(10)
    else:
        print(ans[idx])

t = int(input())

for i in range(t):
    solve()
    
    