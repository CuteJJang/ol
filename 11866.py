n,k = map(int,input().split())
w = -1
cnt = 0
l = [] 
s = 0
for i in range(1,n+1):
    l.append(i)
print("<",end="")
while True:
    w =(w+1) % n
    if l[w] > 0:
        cnt+=1
    if cnt == k:
        if (n-1) == s:
            print(l[w],">",sep="")
        else:
            
            print(l[w],end=", ")
        l[w] = 0
        s+=1
        cnt = 0
    if s == n:
        break

    
        