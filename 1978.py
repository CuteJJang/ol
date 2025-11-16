n = int(input())
l = list(map(int,input().split()))
ans = 0
for k in l:
    if k == 1:
        n-=1
        continue
    for i in range(2,k-1):
        # print(k,i)
        if k % i == 0:
            n = n - 1
            break
print(n)
