l = []

for i in range(8):
    l2 = input()
    l.append(l2)
ans = 0    
for i in range(8):
    for j in range(8):
        if (i + j) % 2== 0 and l[i][j] == "F":
            ans+=1
            
print(ans)    