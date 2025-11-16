n = int(input())
b = 1
ans = 1
while b < n:
    b = b + 6*ans
    ans+=1
print(ans)