def solve():
    n = int(input())
    l = [0,1,1,1,2,2]
    for i in range(6,n+1):
        l.append(l[i-5]+l[i-1])
        
    return l[n]
        
    
t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)

    
    