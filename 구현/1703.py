while True:
    l = list(map(int,input().split()))
    if l[0] == 0:
        break
    s = 1
    c = 2
    ans = 1
    for i in range(l[0]):
        ans = ans * l[s] - l[c]
        s+=2
        c+=2
        
    print(ans)
        
    