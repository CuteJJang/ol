n = int(input())
ans = 0
for i in range(1,n):
    a = i
    b = i
    while b != 0:
        a+=b%10
        b = b // 10
        
    if a ==n:
        ans = i
        break
print(ans)
    
    