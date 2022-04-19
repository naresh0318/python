from operator import index


names = ["Naresh","K Ramlingam","Rawal"]
cnt = 1
names.append("Ranchordas Shaymaldas Chanchad")
for i in range(0,len(names)):
    print(cnt,".",names[i])
    cnt += 1
print(len(names))
names=names[:-1]
print(names[:])