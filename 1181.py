n = int(input())
l = []
for _ in range(n):
    l.append(input())

def mysort(s):
    return len(s) ,s    
l.sort(key=mysort)

prev = ""

for i in range(n):
    if l[i] != prev:
        
        print(l[i])
        prev = l[i]
