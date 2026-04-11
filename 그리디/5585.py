a = 1000 - int(input())
ans = 0
l = [500,100,50,10,5,1]

for i in l:
    ans += a// i
    a = a % i
print(ans)