
name = 'Naresh Sharma'
def vowelscount(name):
    cnt = 0
    for cnt in name:
        if cnt in ['a','e','i','o','u']:
            cnt += 1
    print("total vowels is",cnt)
    return cnt
            

def vovels(name):
    print("user's input is",name)
    for cnt in name:
        if cnt in ['A','E','I','O','U']:
            print(cnt)
    return cnt

vowelscount(name)
vovels(name)


input = str(input())
vovels = ['a','e','i','o','u','A','E','I','O','U']
def vovelscheck():
    print("users's input is = ",input)
    print("vovles are")
    for i in input:
        if i in vovels:
            print(i)
    return i


def vovelcnt():
    cnt = 0
    for i in input:
        if i in vovels:
            cnt += 1
    print("total cnt is = ",cnt)
    return cnt


vovelscheck()
vovelcnt()

    
    