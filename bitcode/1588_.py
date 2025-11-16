n,d = map(int,input().split())
l = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        a = l[i] - l[j]
        if -d <= a <= d:
            ans+=1
print(ans)