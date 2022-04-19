print("enter the number you want to print the table")
user_input = int(input())
for i in range(user_input,user_input+1):
    print("printing table of ",user_input)
    for j in range(1,11):
        print(user_input,"X",j," = ",user_input*j)
