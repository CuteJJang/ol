n,t = map(int,input().split())
l = list(map(int,input().split()))

def chk(k):
    a = 0
    for i in l:
        a+= min(k,i)
    return a

def solve():
    s = 1
    e = t
    ans = 10**10
    while s<=e:
        mid = (s+e)//2
        te = chk(mid)

        if t < te or t == te:
            ans = mid
            e = mid -1
        else:
            s = mid+1

    return ans



print(solve())