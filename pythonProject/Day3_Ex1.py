y = 0
i = 0
while i < 2:
    base = int(input())
    exp = int(input())
    x = pow(base, exp)
    print(x)
    y = y + x
    i += 1
print(y)
