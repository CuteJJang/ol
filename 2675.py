t = int(input())

for i in range(t):
    r,s = input().split()
    r = int(r)
    for c in s:
        for d in range(r):
            print(c,end="")
    
    print()