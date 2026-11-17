def pick_evens(*args):
    sum = []
    for arg in args:
        if arg % 2 == 0:
            sum.append(arg)
    
    return sum

print(pick_evens(5, 10, 15, 12))
