n = int(input())
l = [0] * 10001
for i in range(n):
    a = int(input())
    l[a]+=1

# print(l)

for i in range(len(l)):
    for j in range(l[i]):
        print(i)
        
§