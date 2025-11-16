n = int(input())
f = int(input())

ans = n-n%100   
if ans%f != 0:
    ans = ans + f-ans%f 
    
print(str(ans)[-2:])
    
