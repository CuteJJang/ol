# n = int(input())
# l = [[0] * 101 for _ in range(101)]

# ans = 0
# for i in range(n):
#     y,x = map(int,input().split())
#     for j in range(y,y+10):
#         for k in range(x,x+10):
#             if l[j][k] != 1:
#                 l[j][k] = 1
#                 ans+=1

        
# print(ans)



l = []
for _ in range(100):
    l.append([0]*100)
ans = 0
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            if l[i][j] != 1:
                l[i][j] = 1
                ans+=1
print(ans)