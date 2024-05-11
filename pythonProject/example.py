def even_example(input_var: any):
    input_var = int(input("ENTER NUMBERS"))
    i = 0
    n = 0
    total_even = 0
    new_var  = even_example(5,2,4,6,7)
    array_count = int(len(new_var))
    while i < array_count:
        if (input_var[n])//2:
            total_even += 1
            n += 1
            i += 1
    else:
        print("no even numbers in the list")


