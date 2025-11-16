n,m = map(int,input().split())
l = list(map(int,input().split()))
ans = []
l.sort()

    
def solve(k):
    if k > m:
        print(*ans)
        return
     
    for i in range(n):
        if l[i] == -1:
            continue
        ans.append(l[i])
        l[i] = -1
        solve(k+1)
        l[i] = ans.pop()
        
    return
solve(1)  