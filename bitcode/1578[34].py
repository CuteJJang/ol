n = int(input())
l= list(map(int,input().split()))
ansl = 100
ansm = 1
for i in range(n):
    if l[i] > ansm :
        ansm = l[i]
    if l[i] < ansl:
        ansl = l[i]
print(ansm)
print(ansl)