s = input()
k,c = input().split()
k = int(k)-1
for i in range(len(s)):
    if i ==k:
        print(c,end="")
    else:
        print(s[i],end="")
