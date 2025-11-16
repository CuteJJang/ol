n = int(input())
for i in range(n):
    ans = 0
    l = list(input())
    s = 1
    for c in l:
        if c == "O":
            ans+=s
            s+=1
        else:
            s = 1
    print(ans)