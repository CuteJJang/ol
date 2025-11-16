for _ in range(3):
    ans = 0
    l = list(map(int,input().split()))
    for i in l:
        if i == 1:
            ans+=1
    if ans == 0:
        print("D")
    elif ans == 1:
        print("C")
    elif ans == 2:
        print("B")
    elif ans == 3:
        print("A")
    elif ans ==4:
        print("E")