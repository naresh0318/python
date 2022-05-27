def sum_array(a):
    running_sum = list ()
    running_sum.append(a[0])

    for i in range (1,len(a)):
        running_sum.append(running_sum[i-1]+a[i])

    return running_sum

def solve(running_sum,i,j):
    if i == 0:
        return running_sum[j]
    
    return running_sum[j] - running_sum[i-1]

if __name__ == "__main__":
    a = [1,5,-1,0,4,8,4]
    print("a array = ",a)
    print("sum array = ",sum_array(a))
    running_sum = sum_array(a)


    k = int(input())
    while k > 0:
        i = int(input())
        j = int(input())

        if i >=len(a) or j>=len(a):
            print(-1)
 
        print("Solution is = ",solve(running_sum,i,j))
        k -= 1
