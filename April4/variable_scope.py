# Create a program that defines a variable with the same name as a global variable inside a function and observe its scope.
x = "I'm Great"
def feel():
    x = "I'm Good"
    print(x)
print(x)
feel()
print(x)