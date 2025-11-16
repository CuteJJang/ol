l = list(map(int,input().split()))
ans = 0
for  i in l:
    ans = ans + (i*i)
ans = ans % 10
print(ans)