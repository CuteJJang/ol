n,m = map(int,input().split())
l =  list(map(int,input().split()))
a = [0] * (n+1)
total = 0       

for i in l:
    a[i] = 1
for i in range(1,n+1):
    if a[i] == 0:
        print(i,end=" ") 
        total+=1


if total == 0:
    print(-1)
