def ax(s):
    x = ord(s[0])- ord('A')
    y = int(s[1])-1

    return y,x 

visited = [[0] * 6 for _ in range(6)]
prew = 0,0

d = {
    (2,1),
    (1,2),
    (-1,2),
    (-2,1),
    (-2,-1),
    (-1,-2),
    (1,-2),
    (2,-1)
}

for i in range(36):
    
    t = input()
    y,x = ax(t)

    if i != 0:
        

            for dy,dx in d:
                ny = prew[0] + dy
                nx = prew[1] + dx

                if 0<= ny <= 5 and 0 <= nx <= 5 and visited[ny][nx] == 0 and ny == y and nx == x:
                     





    visited[y][x] = 1
    prew = y,x
