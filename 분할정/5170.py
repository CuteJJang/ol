import sys
input = sys.stdin.readline

n,m = map(int,input().split())

l = list(map(int,input().split()))

s = 0
e = max(l)

def check(k):
    ans = 0
    for i in l:
        if i > k:
            ans+=(i-k)
    return ans

ans = -1
while s<=e:
    mid = (s+e)//2
    t = check(mid)

    if t >=m:
        ans = mid
        s = mid+1
        
    else:
        e = mid-1


print(ans)