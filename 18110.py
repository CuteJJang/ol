n = int(input())
if n == 0:
    print(0)
else:
        
    c = int(n*0.15 // 1)

    if n * 0.15 % 1 >= 0.5:
        c+=1
        
        
    l = [int(input())for _ in range (n)]
    l.sort()
    ans = 0
    for i in range(c,n-c):
        ans +=l[i]
    k = (ans / (n-c-c))
    avg = int(k//1)

    if k % 1  >= 0.5:
        avg+=1
    print(avg)
