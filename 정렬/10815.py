d = {}
input()
l = list(map(int,input().split()))
for i in l:
    d[i] = 1
    
input()
l = list(map(int,input().split()))
for i in l:
    if i in d:
        print(1,end=" ")
    else:
        print(0,end=" ")