def seqfunc(num):
   # num = [5,8,6,1,2,3]
    num = [int,input("enter the numbers ")]
    # num = list(input("Enter the numbers "))
    for i in range(len(num)-2):
        if num[i] == 1 and num[i+1] == 2 and num[i+2] == 3:
            return True
    return False

output = seqfunc(6)
print(output)

