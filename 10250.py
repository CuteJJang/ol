t = int(input())
for k in range(t):
    h,w,n = map(int,input().split())
    cnt = 0
    for x in range(1,w+1):
        for y in range(1,h+1):
            cnt+=1
            if cnt == n:
                s = x + (y*100)
                print(s)
                  