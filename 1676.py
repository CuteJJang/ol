# n = int(input())
# ans = 1
# f = 0
# for i in range(1,n+1):
#      ans=i*ans
# while True:
#      if ans %10 == 0:
#          ans = ans // 10
#          f+=1
#      else:
#          break
# print(f) 
# n = int(input())

# print(n//5)

n = int(input())
ans = 0
i = 5
while True:
    ans+= n //i
    i *= n
        

    