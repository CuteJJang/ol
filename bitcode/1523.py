n = int(input())
l = list(map(int,input().split()))
l2 = l.copy()
l2.reverse()
ans = 1
for i in range(n):
    if l[i] != l2[i]:
        ans = 0
        break
print(ans)