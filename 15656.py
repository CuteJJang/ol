n,m = map(int,input().split())
l = list(map(int,input().split()))
ans = []
l.sort()

    
def solve(k):
    if k > m:
        print(*ans)
        return
     
    for i in range(n):
        ans.append(l[i])
        solve(k+1)
        ans.pop()
        
    return
solve(1)  