#Write a program that modifies a global variable inside a function
x = "Python"
def global_func():
    global x
    x = "Python is interesting to learn"
    print("Now Value of x is: " + x)
print(x)
global_func()
print(x)
