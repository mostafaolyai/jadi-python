


num = int(input())
if 1 > num > 10000:
    print('num should be between 1, 10000')

while num != 1:
    if (num%2) == 0:
        num = num/2
        print(f'num is: {num}')
    elif (num%2) == 1:
        num = (num*3) + 1
        print(f'num is: {num}')
