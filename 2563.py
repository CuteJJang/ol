n = int(input())
l = [[0] * 101 for _ in range(101)]

ans = 0
for i in range(n):
    y,x = map(int,input().split())
    for j in range(y,y+10):
        for k in range(x,x+10):
            if l[j][k] != 1:
                l[j][k] = 1
                ans+=1

        
print(ans)