i = 1
while True:
    a,b,c = map(int,input().split())
    if a==b==c==0:
        break
    
    ans = c//b*a
    ans += min(c%b,a)


    print(f"Case {i}: {ans}")    
    i+=1    