n,q = map(int,input().split())
l = list(map(int,input().split()))
tv = l[0]
tidx = 0
for c in range(n):
    if l[c] > tv:
        tv = l[c]
        tidx = c

L = l[:tidx]
Lset = set(L)
R = l[tidx+1:]
Rset = set(R)

def isLeft(k):
    s = 0
    e = tidx-1

    while s<=e:
        mid = (s+e)//2

        if l[mid] == k:
            return True
        
        elif l[mid] < k:
            s = mid+1
        else:
            e = mid-1
    return False




def isright(k):

    s = tidx+1
    e = n-1

    while s<=e:
        mid = (s+e)//2

        if l[mid] == k:
            return True
        
        elif l[mid] < k:
            e = mid-1

        else:
            s = mid+1

    return False




def solve(k):
    if k == tv:
        print("T")

    elif isLeft(k):
        print("L")

    elif isright(k):
        print("R")

    else:
        print("N")


for _ in range(q):
    a = int(input())
    solve(a)