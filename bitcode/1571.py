n = int(input())
a = list(map(int,input().split()))
ansl = a[0]
ansm = a[0]
ans = 0
for i in a[1:]:
    if i < ansl:
        ansl = i
        ans += 1
    if ansm < i:
        ansm = i
        ans+=1
print(ans)   