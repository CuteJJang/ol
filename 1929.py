m,n = map(int,input().split())

ans = [True] * (n+1)
ans[1] = False


for k in range(2, n+1):
    if ans[k] == False:
        continue
    
    for i in range(k+k, n+1,k):
         ans[i] = False
         
         
for i in range(m,n+1):
    if ans[i] == True:
        print(i)

# for k in range(m,n+1):
#     a = True
#     for i in range(2,k//2+1):
#         if k % i == 0:
#             a = False
#             break
#     if a == True :
#         print(k)
        