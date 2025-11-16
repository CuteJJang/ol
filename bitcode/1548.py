h,m,s = list(map(int,input().split()))
t = h * 60 * 60 + m * 60 + s
ans = 0

for i in range(t+1):
    s = i % 60
    m = i // 60 % 60
    h = i // 60 // 60
    if s % 10 == 1 or s // 10 == 1:
        ans+=1
    elif m % 10 == 1 or m // 10 == 1:
        ans+=1
    elif h % 10 == 1 or h // 10 == 1:
        ans+=1
print(ans)    