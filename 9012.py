t = int(input())
for i in range(t):
    stack = 0
    l = list(input())
    for i in l:
        if i == "(":
            stack+=1
        else:
            stack-=1
        if stack < 0:
            break
            
    if stack == 0:
        print("YES")
    else:
        print("NO")
            
                
    