# n = int(input())
# l = list(map(int,input().split()))
# l.sort()

# m = int(input())

# l2 = list(map(int,input().split()))

# for i in l2:
#     s = 0
#     e = n-1
#     ans = 0

#     while True:
#         if s>e:
#             break
#         mid = (s+e)//2

#         if l[mid] == i:
#             ans = 1
#             break
#         elif l[mid] > i:
#             e = mid-1
#         else:
#             s = mid+1
#     print(ans)








# # from collections import defaultdict


# # n = int(input())
# # a = list(map(int,input().split()))
# # m = int(input())
# # l = list(map(int,input().split()))
# # d = defaultdict(int)
# # for i in a:
# #     d[i]+=1
# # for i in l:
# #     if d[i] == 1:
# #         print(d[i])
# #     else:
# #         print(0)
        

# for i in s:
#     a.add(i)
# m = int(input())

# ss = list(map(int,input().split()))
# for i in ss:
#     if i in a:
#         print(1)
#     else:
#         print(0)




n = int(input())
l = list(map(int,input().split()))
l.sort()

def solve(t):


    s = 0
    e = n-1
    ans = 0
    while s <= e:

        mid = (s+e)//2

        if l[mid] == t:
            ans = 1
            break

        elif l[mid] > t:
            e = mid-1

        else:
            s = mid+1
    print(ans)

m = int(input())

ml = list(map(int,input().split()))
for i in ml:
    solve(i)




