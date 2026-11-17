lst=[]

count = int(input())
for i in range(count):
    lst.append(input().replace('.', ' '))

for i in range(count):
    print(lst[i])