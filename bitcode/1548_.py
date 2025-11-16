h,m,s = map(int,input().split())
d = s+m*60+h*60 *60
ans = 0
for i in range(d+1):
    s = i%60
    m = i//60%60
    h = i//60//60
    if s%10 == 1:
        ans+=1
    elif s //10 == 1:
        ans+=1
    elif m%10 == 1:
        ans+=1
    elif m // 10 == 1:
        ans+=1
    elif h%10 == 1:
        ans+=1
    elif h // 10 == 1:
        ans+=1
print(ans)