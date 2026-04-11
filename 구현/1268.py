n = int(input())

l = [list(map(int,input().split())) for _ in range(n)]
m = 0
s = 0#학생 번호
for i in range(n):
    ans = 0
    cc = [0] * n
    for j in range(5):
        for k in range(n):
            if i == k:
                continue
            if cc[k] == 1:
                continue
            
            if l[i][j] == l[k][j]:
                ans+=1
                cc[k] = 1

                
    if ans > m:
        m = ans
        s = i

print(s+1)

