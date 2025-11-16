ans = 0
s = 0
for i in range(1,5):
    a,b = map(int,input().split())
    ans = ans - a + b 
    if s < ans:
        s = ans 
        
print(s)
    
    