l = list(map(int,input().split()))
l.sort()
n = 1
while True:
    count = 0
    for i in l:
        if n%i == 0:
            count+=1
    if count >= 3:
        print(n)
        break
    else:
        n+=1
                