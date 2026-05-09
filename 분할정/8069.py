import bisect
import sys

input = sys.stdin.readline

n,q = map(int,input().split())
l = list(map(int,input().split()))

for i in range(q):
    a = int(input())

    idx = bisect.bisect_left(l,a)
    if idx == n :
        print(l[-1])

    elif l[idx] == a or idx == 0:
        print(l[idx])
    else:
        left = a-l[idx-1]
        right = l[idx] - a

        if left < right:
            print(l[idx-1])
        elif left == right:
            print(l[idx-1])
        else:
            print(l[idx])
        



    
