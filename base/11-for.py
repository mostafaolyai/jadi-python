step = int(input())
if 1 > step > 20:
    print('step should be between 1, 20')

for _ in range(step):
    num = int(input())
    if 1 > num > 10000:
        print('num should be between 1, 10000')

    if (num%2) == 1:
        num = (num*2) -1
        print(f'num is: {num}')
    elif (num%2) == 0:
        num = num/2
        print(f'num is: {num}')
