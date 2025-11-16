n,d = map(int,input().split())
l = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if -d <= l[i]-l[j] <= d:
            ans+=1
print(ans)