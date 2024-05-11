# Write a program that creates a new tuple containing only the even numbers from a given tuple of integers
x = (6, 7, 9, 10, 4, 8, 15)
t = []
even_tup = ()
for item in x:
    if item % 2 == 0:
        t.append(item)
        even_tup = tuple(t)
print(even_tup)
