a=[1,2,1,2,3,1,2,2,1]
dict = {}
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

print(a)
print(dict)
