
f = open('file.txt', 'a')
f.write('test file\n')
f.close()

f = open('file.txt', 'r')

for line in f:
    print(line)

f.close()
