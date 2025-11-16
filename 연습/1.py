def menofpassion(a, n):
    sum = 0
    cnt=0
    for i in range(1, n):
        for j in range(i+1, n+1):
            sum = sum + a[i] * a[j]
            cnt+=1
    return sum , cnt
print(*menofpassion([1,2,3,4,5,6,7,8],7))