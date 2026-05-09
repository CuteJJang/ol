


# a = []
# n = int(input())
# l = list(map(int,input().split()))
# m = int(input())
# l2 = list(map(int,input().split()))

# s = set(l)

# for i in l2:
#     if i in s:
#         a.append(1)
#     else:
#         a.append(0)

# print(*a,end=" ")

n = int(input())
l = list(map(int,input().split()))
m = int(input())
l.sort()
l2 = list(map(int,input().split()))
def solve(k):
    s = 0
    e = len(l)-1
    ans = 0
    while s <= e:
        mid = (s+e)//2
        if l[mid] == k:
            ans = 1
            break
        elif k < l[mid]:
            e = mid-1

        else:
            s = mid+1

    return ans

for i in l2:
    print(solve(i),end=" ")         


