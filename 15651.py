n,m = map(int,input().split())
ans = []

l = []

for i in range(1,n+1):
    l.append(i)
    
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
 
 