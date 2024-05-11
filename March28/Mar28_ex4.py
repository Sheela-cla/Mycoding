def count_evens():
    count =0
    a = list(map(int,input("Enter the number ").split(" ")))
    for i in range(len(a)):
        if a[i]%2 == 0:
            count += 1
    return(count)


output = count_evens()
print(output)
