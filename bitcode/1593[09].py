n = int(input())
h = list(map(int,input().split()))
l = [0] * (n+1)
ans = 0
for i in range(n):
    s = h[i]
    l[s] = 1

for i in range(1,n+1):
    if l[i] == 0:
        ans+=1
print(ans)  
