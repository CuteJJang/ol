t = int(input())
l = list(map(int,input().split()))
Y = 0
M = 0
for i in l:
    Y += (i// 30 *10 ) + 10
    M +=(i// 60 * 15 ) +15
    
if Y < M:
    print("Y",Y)
elif Y > M:
    print("M",M)
else:
    print("Y M",Y) 