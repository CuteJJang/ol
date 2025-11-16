n = int(input())
s = 1
b = n - 1
for i in range(n):
    print(" "*b+"*"*s)
    b = b - 1
    s = s + 2
b=b+1
s=s-2
b=b+1
s=s-2
for i in range(n-1):
    print(" "*b+"*"*s)
    b = b + 1
    s = s - 2
