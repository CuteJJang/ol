n,m = map(int,input().split())
ans = []

l = []

for i in range(1,n+1):
    l.append(i)
    
def solve(k,kk):
    if k > m:
        print(*ans)
        return
     
    for i in range(kk,n):
        ans.append(l[i])
        solve(k+1, i )
        ans.pop()
    return
solve(1,0)       
 
 