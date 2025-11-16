n = int(input())
s = list(map(int,input().split()))

# for i in range(n):
#     d = max(s)
#     e = min(s)
# print(d,e,sep ="\n")
vmax = 1
vmin = 100
for i in s:
    if vmin > i:
        vmin = i
    if vmax < i:
        vmax = i
print(vmax,vmin,sep="\n")