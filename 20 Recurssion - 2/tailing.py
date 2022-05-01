def Tailing (N):
    if N < 0:
        return 0

    if N == 0:
        return 1

    ans = Tailing(N-1) + Tailing(N-2)
    return ans

print(Tailing(9))