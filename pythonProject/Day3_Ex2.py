# Write a program that calculates the sum of all elements in a given tuple.
tup = (2, 3, 5, 10, 30)
value = (len(tup))
total = 0
i = 0
while i < value:
    total = total + tup[i]
    i += 1
print("The sum of all tuple elements : " + str(total))
