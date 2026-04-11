n = int(input())
d = {}
for i in range(n):
    a = input().split()
    f = True
    s = ""
    for j in a:

        if f and j[0].lower() not in d:

            d[j[0].lower()] = 1

            if s == "":

                s =  "["+j[0]+"]"+j[1:]
            else:
                s = s + " " + "["+j[0]+"]"+j[1:]
            # print("["+j[0]+"]"+j[1:],end=" ")
            f = False
        else:
            if s != "":

                s = s + " "+j

            else:

                s =  j
    
    if f == False:

        print(s)
        continue
    f = True    
    c = ""
    for j in a:
        for k in j:
            if f and  k.lower() not in d:
                d[k.lower()] = 1
                c = c + "["+k+"]"
                f = False
            else:
                c = c + k
        c = c + " "
    
    print(c)