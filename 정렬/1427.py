s = input()
l = []

for i in s:
    l.append(int(i))
    
l.sort(reverse=True)
for i in l:
    print(i,end="")
