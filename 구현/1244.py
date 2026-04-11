n = int(input())
l = [0] + list(map(int,input().split()))
m = int(input())

def solve():
    a,b = map(int,input().split())
    if a == 1:
        for i in range(b,n+1,b):
    
    
            l[i] = (l[i] + 1) % 2
    else:
        ll,rr = b,b
        l[ll] = (l[ll]+1) % 2
        while 0 < ll and n >= rr and l[ll] == l[rr]:
            l[ll] = (l[ll]+1) % 2
            l[rr] = (l[rr]+1) % 2
            ll-=1
            rr+=1

            
    
    




for î in range(m):
    solve()

for i in range(1,n+1,20):
    print(*l[i : i+20])
