def stringbits(my_string):
    return my_string[::2]
test_string = ["hello","hi"]
results=[stringbits(my_string) for my_string in test_string]
print(results)