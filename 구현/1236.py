n,m = map(int,input().split())
l = []
for i in range(n):
    a  = input()
    l.append(a)
    
ans1 = 0
for i in range(n):
    isx = False
    for j in range(m):
        if l[i][j] == "X":
            isx = True
            break
    if isx == False:
        ans1+=1
        
ans = 0
for j in range(m):
    isx = False
    for i in range(n):
        if l[i][j] == "X":
            isx = True
            break
    if isx == False:
        ans+=1
        
print(max(ans1,ans))          
    