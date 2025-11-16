
x = 0
y = 0
ansm = -1

l = [list(map(int,input().split())) for i in range(9)]

for i in range(9):
    for j in range(9):
        if ansm <= l[i][j]:
            y = i
            x = j
            ansm = l[i][j]
            
print(ansm)
print(y+1,x+1)