while True:
    l = list(map(int,input().split()))
    l.sort()
    a,b,c = l
    
    if a == 0 and b == 0 and c == 0:
        break
    elif a == 0:
        print("wrong")
    elif b == 0:
        print("wrong")
    elif c == 0:
        print("wrong")
    
    
    elif (a*a)+(b*b) == (c*c):
        print("right")
    else:
        print("wrong")
        