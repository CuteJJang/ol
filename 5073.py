while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    l = [a,b,c]
    l.sort()
    if l[2] >= (l[0]+l[1]):
            print("Invalid") 
    else:
        if a == b and b == c:
            print("Equilateral")
        elif a == b or b == c or a ==c:
            print("Isosceles")
        else:
            print("Scalene")
            