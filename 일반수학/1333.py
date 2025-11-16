n,l,d = map(int,input().split())
ans = [1] * 4000
idx = 0
for i in range(n):
    for j in range(l):
        ans[idx] = 0
        idx+=1
    idx+=5
g =d
while True:
    if ans[d] == 1:
        print(d)
        break
    
    d+=g
    
