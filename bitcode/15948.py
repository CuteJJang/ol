a,b,c = map(int,input().split())
ac = c - a
cb = b - c
if ac <= cb :
    print("A")
else:
    print("B")
