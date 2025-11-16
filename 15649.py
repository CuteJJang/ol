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
        if l[i] < 1:
            continue
        
        ans.append(l[i])
        l[i] = 0
        solve(k+1)
        l[i] = ans.pop()
 
 
 
solve(1)       