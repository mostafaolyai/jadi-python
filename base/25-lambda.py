def pick_evens(*args):
    sum = []
    for arg in args:
        if arg % 2 == 0:
            sum.append(arg)
    
    return sum

print(pick_evens(5, 10, 15, 12))

#anonymose function

print(list(filter(lambda x: x%2==0, (5, 10, 15, 12))))

#new use
multiply = lambda x, y: x * y
print(multiply(3, 4))
