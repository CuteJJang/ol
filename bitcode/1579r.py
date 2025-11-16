n = int(input())
s = []
for i in range(1,n+1):
    s.append(i)
while True:
    if len(s) == 1:
        break 
    s.append(s[0])
    s = s[2:]
print(s[0])