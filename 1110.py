n = int(input())
ans = 0
c = n
while True:
    ans+=1
    a = c //10
    b = c%10
    c = b*10+(a+b)%10
    if c == n:
        break
print(ans)
