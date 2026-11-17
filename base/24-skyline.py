def skyline(*args):
    max = 0
    for arg in args:
        if arg > max:
            max = arg
    
    return max

print(skyline(5, 10, 15, 12))
