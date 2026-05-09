n,m = map(int,input().split())
l = list(map(int,input().split()))
s = 0
aa = 0 
for i in range(len(l)):
    if l[i] > s:
        s = l[i]
        aa = i



def bs(s,e,k):
    while s<= e:
        mid = (s+e)//2

        if k == l[mid]:
            return 1
        elif k > l[mid]:
            s = mid+1

        else:
            e = mid -1

    return 0

def bs2(s,e,k):
    while s<= e:
        mid = (s+e)//2

        if k == l[mid]:
            return 1
        elif k < l[mid]:
            s = mid+1

        else:
            e = mid -1

    return 0
    

for i in range(m):
    a = int(input())
    if s == a:
        print("T")
    elif bs(0,aa-1,a) == True:
        print("L")

    elif bs2(aa+1,len(l)-1,a) == True:
        print("R")


    else:
        print("N")