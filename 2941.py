l = ["c=","c-","dz=","d-","lj","nj","s=","z="]
# s = input()
s = input()
for c in l:
    s = s.replace(c,'a')
print(len(s))