l = [2, 0, -9, 9, 7]

new_l = [n * 2 for n in l]

print(new_l)

#--------------------------------
a = 5

res = 'Zoj' if a%2 == 0 else 'Fard'
print(res)

#--------------------------------
l = [2, 1, -9, 0, 7]

new_l2 = ['Zoj' if n%2 == 0 else 'Fard' for n in l]

print(new_l2)

#--------------------------------