n = int(input())
p = 0
if n == 1:
    p = 100000000
elif n == 2:
    p = 35000000
elif n <= 5:
    p = 30000000
elif n <= 10:
    p = 10000000
elif n <= 20:
    p = 1000000
print(p)