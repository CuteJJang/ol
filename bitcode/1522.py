n, m = map(int,input().split())
l = list(map(int,input().split()))
f = [0] * (m+1)
for i in l:
    f[i] +=1
ans = 0
for i in range(1, m+1):
    if f[i]==0:
        print(i,end=" ")
        ans=1
if ans == 0:
    print(-1)
