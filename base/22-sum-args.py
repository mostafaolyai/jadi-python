def sum_numbers(*args):
    sum = 0
    for arg in args:
        sum += arg
    
    return sum

print(sum_numbers(5, 10, 15))
