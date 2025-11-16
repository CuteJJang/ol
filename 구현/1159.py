t = int(input())
l = [0] * 26
for i in range(t):
    s = input()
    l[ord(s[0])-ord('a')]+=1
d = "False"
for i in range(len(l)):
    if l[i] >= 5:
        k = i + ord('a')
        print(chr(k),end="")
        d = "True"
        
if d == "False":
    print("PREDAJA") 
        
    