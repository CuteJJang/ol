n,m,M,t,r = map(int,input().split())
b = m
ans = 0
a = 0
c = 0

if m + t > M:
    print(-1)
else:    
    while True:
        if a ==n:
            break
        if b+t <=M:
            a+=1
            ans+=1
            b = b +t
        else:
            c+=1
            ans+=1
            b = max(b-r,m)
    print(ans)  