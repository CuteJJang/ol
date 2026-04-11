n,m = map(int,input().split())

r = [list(map(int,input()))for _ in range(n)]

ans =   1
# print(*r,sep="\n")
def solve(y,x):
    ans = 1
    for d in range(1,51):
        nx = x + d
        ny = y + d

        if 0 <= ny < n and 0 <= nx < m :
            if r[y][x] == r[ny][nx]  == r[ny][x]  == r[y][nx]:
                ans = d+1
                


        else:
            break                

    return ans*ans


for i in range(n):
    for j in range(m):

        ans = max( ans,solve(i,j))


print(ans)