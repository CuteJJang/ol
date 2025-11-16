n = int(input())

k = 1
gap = 2
while n > k:
    k+=gap
    gap +=1
gap-=1
d = k - n
if gap % 2 == 0:
    m = gap - d
    z = 1 + d
else:
    m = 1 + d
    z = gap - d
print(f"{m}/{z}")

