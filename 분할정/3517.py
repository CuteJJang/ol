n = int(input())
l = list(map(int,input().split()))
m = int(input())
l2 = list(map(int,input().split()))

def solve(k):
    #k 반환 큐티 미미미미미미미미미치고 싶탕아앙
    id = -1
    s  = 0 
    e = len(l)-1

    while s <= e:
        mid = (s+e)//2
        if l[mid] == k:
            id = mid
            break
        elif l[mid]> k:
            e = mid-1
        else:
            s = mid+1

    return id




for c in l2:
    print(solve(c),end=" ")