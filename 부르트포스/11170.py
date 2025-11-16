t = int(input())
for i in range(t):
    ans = 0
    n,m = map(int,input().split())
    for j in range(n,m+1):
        j = str(j)
        for k in j:
            if k == "0":
                ans+=1
                
    print(ans)