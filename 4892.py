idx = 0
while True:
    n = int(input())
    if n == 0:
        break

    n1 = n * 3
    if n1 % 2 == 0:    
        n2 = n1 // 2
    else:
        n2 = (n1+1) // 2
    
    n3 = n2 * 3
    n4 = n3 // 9
    if n1 % 2 == 0:
        n = n4 * 2
        idx = idx + 1
        print(f"{idx}. even {n4}")
    else:
        n = n4 *2 + 1
        idx = idx + 1
        print(f"{idx}. odd {n4}")
