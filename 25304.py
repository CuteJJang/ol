x = int(input())
n = int(input())
s = 0
for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    s = s + a * b


if s == x:
    print("Yes")
else:
    print("No")
