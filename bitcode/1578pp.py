n = int(input())
l = list(map(int,input().split()))
ansm = 1
ansl = 100
for i in range(n):
    if l[i] > ansm:
        ansm = l[i]
    if l[i] < ansl:
        ansl = l[i]
print(ansm)
print(ansl)