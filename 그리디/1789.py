s = int(input())
cnt = 0
ans = 0
while True:
    if ans > s:
        break
    cnt +=1
    ans+=cnt
print(cnt-1)