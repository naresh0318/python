def solve(s):
    empty_dict = dict()
    n = len(s)

    max_length = 0
    start = 0
    end = 0

    while end < n:
        if s[end] not in empty_dict:
            empty_dict[s[end]] = end
            length = end - start + 1
            max_length  = max(max_length, length)
            end += 1
        
        else:
            while s[end] in empty_dict:
                empty_dict.pop[s[start]]
                start += 1
            empty_dict[s[end]] = end
            end += 1

    return max_length

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    print(solve(s))