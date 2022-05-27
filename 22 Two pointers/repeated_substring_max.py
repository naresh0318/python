def is_repeated(s):
    repeat = dict()
    for i in s:
        if i not in repeat:
            repeat[i] = 1

        else:
            return True

    return False


def solve(str):         
    n = len(str)
    max_len = 0
    for i in range(n):
        for j in range(i,n):
            s = str[i:j]
            if not is_repeated(s):
                max_len = max(max_len,len(s))

    return max_len

if __name__ == "__main__": 
    print(solve("ADOBECODEBANC"))  