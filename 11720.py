n = int(input())
s = int(input())

ans = 0

while s != 0:
    r = s % 10
    ans = ans + r
    s = s//10

print(ans)
    