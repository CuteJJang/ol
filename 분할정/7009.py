n,m = map(int,input().split())
l = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l.sort()

def solve(k):
    s = 0 
    e = len(l)-1
    while s<=e:
        mid  = (s+e)//2
        if l[mid] == k:
            return 1
        elif l[mid] > k:
            e = mid-1 
        else:
            s = mid+1
    return -1

cnt = 0 
for c in l2:
    s = solve(c)
    if s== -1:
        print(c,end=" ")
        cnt +=1

if cnt==0:
    print(-1)

