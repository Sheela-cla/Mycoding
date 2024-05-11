# Write a function that takes a list of numbers and returns a list containing the squares of each number using lambda.
sqr_list = [2,3,4,5,6]
answer = list(map(lambda x: x**2,sqr_list))
print(answer)