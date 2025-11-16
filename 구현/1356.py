s = input()
a = 1
b = 1
z = 0


if len(s) == 1:
    print("NO")
    exit()


for i in s:
    if int(i) == 0:
        z+=1
    a = a * int(i)

if z == 1:
    print("NO")
elif z >= 2:
    print("YES")
else:
    
    f = "False"

    
    for i in s:
        a = a // int(i)
        b = b * int(i)
        if a == b:
            f = "True"
            break
    if f == "True":
        print("YES")
    else:
        print("NO")
    
