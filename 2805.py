n,m = map(int,input().split())

l = list(map(int,input().split()))

s = 0
e = 2_00000_0000
ans = 0
while True:
    if s > e:
        break

    mid = (s+e)//2
    a = 0
    for i in l:
        a+= max(0,i-mid)

    if a >= m:
        ans = mid
        s = mid+1

    else:
        e = mid-1

print(ans)
    

