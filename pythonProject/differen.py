def differ_var(n):
    diff = 21 - n

    if n > 21:
        diff = diff * 2
    return diff


print(differ_var(31))
