n = int(input())

def 이면수(k):
    if k < 6:
        return False
    ss = 0
    while k != 0:
        ss +=k %10
        k =  k //10
    if ss % 2 == 0:
        return False
    
    return True

def 임현수(k):
    if k == 2 and k == 4:
        return True
    t = k
    cnt = 0
    cnt2 = 0
    for i in range(2,k+1):
        if t % i == 0:
            cnt +=1
            while t % i == 0:
                t = t // i
                cnt2 +=1

    if cnt2 == 1:
        return False
    if cnt % 2 == 0:
        return True
    



    return False    


a,b = 이면수(n),임현수(n)

if a == True and b == True:
    print(4)
elif a == False and b == False:
    print(3)
elif a == True and b == False:
    print(1)
else:
    print(2)