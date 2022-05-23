"""
# merge sorting..
C = list()
def merge_sorting(A,B):
    for i in A:
        C.append(i)

    for i in B:
        C.append(i)

    C.sort()
    return C

if __name__ == "__main__":
    print(merge_sorting([12,34,56,78],[0,2,4,789,899,999]))

"""

def p1p2(a,b):
    p1 = 0
    p2 = 0
    n = len(a)
    m = len(b)
    c = list()

    while p1<n and p2<m:
        if a[p1] < b[p2]:
            c.append(a[p1])
            p1 += 1

        else:
            c.append(b[p2])
            p2 += 1

    while p1<n:
        c.append(a[p1])
        p1 += 1
    while p2<m:
        c.append(a[p2])
        p2 += 1

    return c

if __name__ == "__main__":
    print(p1p2([12,23,34,45],[1,2,3,4,5]))

