# Write a function that returns a list of prime numbers up to a given number using lambda.
# num = 40
lst = filter(lambda x: all(x%y != 0 for y in range(2,x)),range(2,40))
print(list(lst))