n = int(input())
ansj = 0
ansg = 0
for i in range(n):
    a = input().rstrip()
    if a == "A":
        ansj+=1
    if a == "B":
        ansg+=1
# print(ansj, ansg)        
if ansj > ansg :
    print("A")
else:
    print("B")