while True:
    ans = 0
    l = []
    n = int(input())
    if n == -1 :
        break
    for i in range(1,n):
        if n % i == 0:
            l.append(i)
            ans+=i
    if n != ans:
        print(f"{n} is NOT perfect.")
    else:
        print(f'{n} = ',end="")
        print(*l,sep=" + ")
        