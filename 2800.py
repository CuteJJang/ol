def solve():


    n,m = map(int,input().split())
    l = list(map(int,input().split()))

    left = 0
    right = max(l)
    ans = 0
    while True:
        if left > right :
            break
        mid = (left+right)//2
        w = 0
        for i in l:
            w += max(0,i-mid)
        if w >= m:
            ans = mid
            left = mid+1
        else:
        
            right = mid-1

    print(ans)
solve()