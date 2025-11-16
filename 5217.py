t = int(input())
for i in range(t):
    n = int(input())
    print(f"Pairs for {n}:", end = " ")
    first = 0
    for c in range(1,n+1):
        ans = n - c
        if c < ans:
            if first == 0:
                print(c,ans, end ="")
                first = 1
            else:
                print("," ,c,ans,end = "")
    print()

