s = int(input())
if str(s)[-1] != "0":
    print(-1)
    exit()
print(s//300,end=" ")
print((s%300)//60,end= " ")
print((s%60)//10,end=" ")