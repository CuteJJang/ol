m = int(input())
n = int(input())
l = 0
min = n
for k in range(m,n+1):
    if k == 1:
        continue
    check = 0
    for i in range(2,k-1):
        if k % i == 0:
            check = 1
            break
    
    if check == 0:
        #k는 소수
        l +=k
        if k < min:
            min  = k
if l == 0:
    print(-1)
else:
    print(l,min,sep="\n")
        
        
            
            
    