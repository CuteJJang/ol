while True:
    s = list(input().split())
    if s[0] == "#":
        break
    s[1] = int(s[1])
    s[2] = int(s[2])
    
    if s[1] > 17 or s[2] >= 80:
        print(f"{s[0]} Senior")
    else: 
        print(f"{s[0]} Junior")
    