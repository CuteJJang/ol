l = [1] * 10001
for i in range(1,10000+1):
    if l[i] == 1:
        print(i) 
    ans = i
    k = i
    while k != 0:
        ans+=k%10
        k = k //10
    if ans <=10000:
        l[ans] = 0
        
        