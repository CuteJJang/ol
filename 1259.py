while True:
    s = input()
    if s ==  "0":
        break
    l = 0
    r = len(s) -1
    while l <= r:
        if s[l] == s[r]:
            l+=1
            r-=1
        else:
            break
            
    if l>r:
        print("yes")
        
    else:
        print ("no")
        