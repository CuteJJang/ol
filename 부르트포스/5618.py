t = int(input())
l = list(map(int,input().split()))
for i in range(1,min(l)+1):
    s = False
    for j in l:
        if j % i == 0:
            s = True
        else:
            s = False
            break
    if s == True:
        print(i)
    