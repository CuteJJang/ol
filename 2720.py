t = int(input())
for i in range(t):
    p = int(input())
    for c in [25,10,5,1]:
        print(p//c,end=" ")
        p = p% c
    print()