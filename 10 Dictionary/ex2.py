from os import lseek


vote = ["BJP","CONGRESS","BJP","AAP","AAP","BJP","BJP"]
print(vote)
cnt ={}
for i in vote:
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1
print(cnt)

#getting maximum value........
votes=0
winning_party = ""
for i in cnt.keys():
    if votes<cnt[i]:
        votes=cnt[i]
        winning_party = i
print(winning_party)
if votes == cnt["BJP"]:
    print("MODI Sarkar")
elif votes == cnt["CONGRESS"]:
    print("PAPPU'S SARKER")
else :
    print("AAM AADMI PARTY")