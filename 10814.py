n = int(input())

p=[]

for i in range(1,n+1):
    a,b = input().split()
    a=  int(a)
    p.append([a,i,b])
p.sort()
for i in p:
    print(i[0],i[2])