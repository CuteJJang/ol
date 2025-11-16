y1,m1,d1 = list(map(int,input().split("/")))
y2,m2,d2 = list(map(int,input().split("/")))
m1 = m1 + (y1 * 12)
m2 = m2 + (y2 * 12)
if d1 > d2:
    m2 = m2 - 1

ans = m2-m1

if ans >= 12:
    ans = ans // 12
    print(ans,"Y",sep="")
else:
    print(ans,"M",sep="")