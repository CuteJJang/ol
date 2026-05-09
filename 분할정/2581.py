n = int(input())
l = list(map(int,input().split()))
m = int(input())


def check(k):
    ans = 0
    for i in l:
        ans+= min(i,k)

    return ans

s = 0
e = max(l)
ans = 0
while s<= e:
    mid = (s+e)//2
    t = check(mid)

    if t <= m:
        ans = mid
        s = mid+1

    else:
        e = mid-1


print(ans)
