a,b,c,n = map(int,input().split())

for i in range(n//a+1):
    for j in range(n//b+1):
        for k in range(n//c+1):
            t = a*i +b*j + c*k
            if t == n:
                print(1)
                exit()
                
print(0)            