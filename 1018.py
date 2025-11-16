n,m = map(int,input().split())
l = [list(input()) for _ in range(n)]

def cn(y,x):
    bstart = 0
    wstart = 0
    for yy in range(y,y+8):
        for xx in range(x,x+8):
            if (yy+xx)% 2 == 0:
                if l[yy][xx] == "W":
                    bstart+=1
                else:
                    wstart+=1
            else:
                if l[yy][xx] == "B":
                    bstart+=1
                else:
                    wstart+=1
    return  min(bstart,wstart)               
                
ans = 1e19
for i in range(n-7):
    for j in range(m-7):
            ans = min(ans, cn(i,j))
print(ans)