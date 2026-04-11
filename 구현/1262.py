n,y1,x1,y2,x2 = map(int,input().split())

def solve(y,x):
    y = y % (2*n-1)
    x = x % (2*n-1)

    d = abs(y-(n-1)) + abs(x-(n-1))

    if d >= n:
        return '.'
    c = chr(ord('a') + (d%26))
    return c 

for i in range(y1,y2+1):
    for j in range(x1,x2+1):
        print(solve(i,j),end="")
    print()