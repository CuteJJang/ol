sub = 0
score = 0
for _ in range(20):
    a,b,c = input().split()
    b = int(b[0])
    if c != 'P':
        sub = sub + b

    if c == 'A+':
        score = score + b*4.5
    elif c == 'A0':
        score = score + b*4.0
    elif c == 'B+':
        score = score + b*3.5
    elif c == 'B0':
        score = score + b*3.0
    elif c == 'C+':
        score = score + b*2.5
    elif c == 'C0':
        score = score + b*2.0
    elif c == 'D+':
        score = score + b*1.5 
    elif c == 'D0':
        score = score + b*1.0
    else:
        score = score + b*0  
print(score/sub)    