n = int(input())
l = []
t = 0
for i in range(n):
    s = input()
    l.append(s)
    t = len(s)
    
    
for j in range(t):
    c = l[0][j]
    for i in range(1,n):
        if l[i][j] != c:
            c = "?"
            break
    print(c,end="")    