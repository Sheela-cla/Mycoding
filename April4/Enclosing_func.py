# Create a program that defines a function within another function and access variables from the outer function.
# (Often called Enclosing Scope)

x = 10
print("I'm global variable and my value is: ",x)
def add():
    x = 20
    print("I'm Local variable and my value is: ",x)
    def add_extend():
        y = x + 5
        print ("I'm Enclosing function and I use local_var X in outer function & my value is : ", y)
    add_extend()
add()

