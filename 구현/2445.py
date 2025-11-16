n = int(input())


for i in range(1,n+1):
    s = "*" * i
    e = " " * (n-i)
    print(s+e+e+s)
    
    
for i in range(1,n):
    a = "*" * (n-i)
    b = " " * i
    print(a+b+b+a)
    