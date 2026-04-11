n = int(input())

ans = 1e10
c5 = 0
while True:
    if n < c5*5:
        break
    n2 = n - c5*5
    if n2 % 2 == 0:
        ans = min(ans,n2 // 2 + c5)
    c5+=1

if ans == 1e10:
    print(-1)
else:
    print(ans)