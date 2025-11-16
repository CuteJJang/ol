n = int(input())
d= -1
c = -1
for i  in range(n):
    a = 0 
    s = list(map(int,input().split()))
    for j in range(0,5):
        for k in range(j+1,5):
            for t in  range(k+1,5):
                f = (s[j]+s[k]+s[t])%10
                if a < f:
                    a = f
    if c <= a:
        c = a
        d = i
print(d+1)                
                    