# n = int(input())
# l = [-1] * 5006
# l[3] = 1
# l[5] = 1
# for i in range(3,n+1):
#     if l[i] != -1:
#         if l[i]+1 < l[i+3] or l[i+3] == -1:
#             l[i+3] = l[i]+1
#         if l[i]+1 < l[i+5] or l[i+5] == -1:
#             l[i+5] = l[i]+1
# print(l[n])

# n = int(input())
# l = [-1] * (n+6)
# l[0] = 0
# for i in range(n):
#     if l[i] == -1:
#         continue
    
#     if l[i+3] == -1:

#         l[i+3] = l[i] + 1
#     else:
#         l[i+3] = min(l[i+3], l[i] + 1)
#     if l[i+5] == -1:
        
#         l[i+5] = l[i] + 1
# print(l[n])

n = int(input())
l = [1e99999]*(n+6)
l[0]=0
l[3] = 1
l[5] = 1
for i in range(6,n+1):
    l[i] = min(l[i-3]+1,l[i-5]+1)
if l[n] == 1e99999:
    print(-1)
else:
    print(l[n])