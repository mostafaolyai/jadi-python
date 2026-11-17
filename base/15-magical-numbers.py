num = int(input())

if (num % 3 == 0) and (num % 5 == 0):
    print('افسانه ای')

elif (num % 3 == 0):
    print('جادویی')

elif (num % 5 == 0):
    print('نفرین شده')

else: print('معمولی')
