k = int(input())
n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
    ans = ans + a[i]
if ans <= k:
    print("YES")
else:
    print("NO")